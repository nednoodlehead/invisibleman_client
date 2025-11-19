import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from db.fetch import fetch_by_variable
matplotlib.use("Qt5Agg")  # i think this is important...


class DataCanvas(FigureCanvasQTAgg):

    def __init__(
        self, conn=None, parent=None, width=15, height=4, dpi=100, height_2=290, width_2=790
    ):
        self.connection = conn
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111)
        super(DataCanvas, self).__init__(self.figure)
        self.setParent(parent)
        self.setFixedWidth(width_2)
        self.setFixedHeight(height_2)

    def set_bar_graph(
        self, bar_name: [str], bar_values: [int], data_choice: str
    ):  # accurate params..
        self.axes.cla()  # clears the data stuff
        self.axes.set_title(data_choice)
        self.axes.bar(
            bar_name, bar_values, color="maroon", width=0.2, align="edge"
        )  # changes to bar with the stuff
        self.axes
        self.draw()

    def set_pie_chart(self, names: [str], values: [str], data_choice: str):
        self.axes.cla()
        self.axes.set_title(data_choice)
        wedges = self.axes.pie(values, autopct="%1.1f%%")
        self.axes.legend(
            wedges[0], names, loc=(0.90, -0.1)
        )  # place the legend a bit above and to the right of pie
        self.draw()

    def set_donut_chart(self, names: [str], values: [str], data_choice: str):
        self.axes.cla()
        self.axes.set_title(data_choice)
        wedges = self.axes.pie(values, wedgeprops=dict(width=0.5), autopct="%1.1f%%")
        self.axes.legend(wedges[0], names, loc=(0.90, -0.1))
        self.draw()

    def set_line_graph(self, names: [str], values: [str], data_choice: str):
        self.axes.cla()
        self.axes.set_title(data_choice)
        self.axes.plot(values)
        names = list(names)
        for count, val in enumerate(values):
            self.axes.text(count, val, names[count])
        self.draw()

    def swap_theme(self, is_dark: bool):
        # idk if this is possible..
        # redraw and change the params when making the graph, maybe have on thread...
        pass

    def change_graph(self, data_choice: str, graph_choice: str):
        data = self.fetch_from_db_and_insert(data_choice)
        if graph_choice == "Bar":
            self.set_bar_graph(data.keys(), data.values(), data_choice)
        elif graph_choice == "Pie":
            self.set_pie_chart(data.keys(), data.values(), data_choice)
        elif graph_choice == "Line":
            self.set_line_graph(data.keys(), data.values(), data_choice)
        elif graph_choice == "Donut":
            self.set_donut_chart(data.keys(), data.values(), data_choice)
        else:
            # i dont think this can even be hit lmao
            # 3/12/2025 - i hit this valuerror. im so proud
            
            print(f'data: {data_choice} graph={graph_choice}')
            raise ValueError("how did you get this ?")

    def fetch_from_db_and_insert(self, name: str) -> dict:  #
        # name = one of the `self.acceptable_all_charts` options
        # thread this !?
        # maybe this is sort of stupid to fetch all, then goof with the data,
        # would be better to select only relevant fields, then goof with it
        # match name:
        #     case "Asset Type":
        x = dict(fetch_by_variable(self.connection, name))
        print(x)
        return x
                
                
        # property_to_int = {
        #     "Asset Type": 0,
        #     "Manufacturer": 1,
        #     "Serial Number": 2,
        #     "Model": 3,
        #     "Cost": 4,
        #     "Assigned To": 5,
        #     "Asset Location": 6,
        #     "Asset Category": 7,
        #     "Deployment Date": 8,
        #     "Replacement Date": 9,
        #     # retirement date would go here...
        #     "Notes": 10,
        # }
        # vals = {}
        # raw_data = fetch_all(self.connection)
        # if (
        #     name == "Notes"
        # ):  # for notes, we separate into has notes, or doesn't have notes
        #     vals["Some Notes"] = 0
        #     vals["No Notes"] = 0
        #     for obj in raw_data:
        #         if obj.notes == "":
        #             vals["No Notes"] += 1
        #         else:
        #             vals["Some Notes"] += 1
        # # should sort this list, so it makes sense when viewing...
        # elif name == "Deployment Date":  # all data should be like: 2024-09-24
        #     raw_data = sorted(raw_data, key=lambda x: x.deploymentdate)
        #     for obj in raw_data:
        #         # use to have: - {months[obj.purchasedate[5:7]]}
        #         value = f"{obj.deploymentdate[:4]}"
        #         if value not in vals:
        #             vals[value] = 1
        #         else:
        #             vals[value] += 1
        # elif name == "Replacement Date":
        #     sorted(raw_data, key=lambda x: x.replacementdate)
        #     for obj in raw_data:
        #         value = f"{obj.replacementdate[:4]}"
        #         if value not in vals:
        #             vals[value] = 1
        #         else:
        #             vals[value] += 1
        # elif name == "Replacement Date":  maybe something special for retirement? TODO
        #     raw_data = sorted(raw_data, key=lambda x: x.replacementdate)
        #     for obj in raw_data:
        #         value = f"{obj.replacementdate[:4]}"
        #         if value not in vals:
        #             vals[value] = 1
        #         else:
        #             vals[value] += 1

        # else:
        #     for obj in raw_data:
        #         for count, data in enumerate(obj):
        #             if count == property_to_int[name]:
        #                 if data not in vals:
        #                     vals[data] = 1
        #                 else:
        #                     vals[data] += 1
        # return vals


# https://stackoverflow.com/questions/60659643/how-to-change-the-background-colour-of-a-cell-in-a-qcalendarwidget-using-an-sql
# https://www.pythonguis.com/tutorials/plotting-matplotlib/
