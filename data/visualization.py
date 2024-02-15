import matplotlib
matplotlib.use("Qt5Agg")  # i think this is important... 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot
from db.fetch import fetch_all

class DataCanvas(FigureCanvasQTAgg):

     def __init__(self, parent=None, width=15, height=4, dpi=100, height_2=290, width_2=790):
          self.figure = Figure(figsize=(width, height), dpi=dpi)
          self.axes = self.figure.add_subplot(111)
          super(DataCanvas, self).__init__(self.figure)
          self.setParent(parent)
          self.setFixedWidth(width_2)
          self.setFixedHeight(height_2)

     def set_bar_graph(self, bar_name: [str], bar_values: [int], data_choice: str):  # accurate params..
          self.axes.cla()  # clears the data stuff
          self.axes.set_title(data_choice)
          self.axes.bar(bar_name, bar_values, color='maroon', width=0.2, align='edge')  # changes to bar with the stuff
          self.axes
          self.draw()

     def set_pie_chart(self, names: [str], values: [str], data_choice: str):
          self.axes.cla()
          self.axes.set_title(data_choice)
          wedges = self.axes.pie(values, autopct='%1.1f%%')
          self.axes.legend(wedges[0], names, loc=(.90, -0.1))  # place the legend a bit above and to the right of pie
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

     def change_graph(self, data_choice: int, graph_choice: str):
          data = self.fetch_from_db_and_insert(data_choice)
          if graph_choice == "Bar":
               self.set_bar_graph(data.keys(), data.values(), data_choice)
          elif graph_choice == "Pie":
               self.set_pie_chart(data.keys(), data.values(), data_choice)
          elif graph_choice == "Line":
               self.set_line_graph(data.keys(), data.values(), data_choice)

     def fetch_from_db_and_insert(self, name: str) -> dict:  #  
          # thread this !?
          # maybe this is sort of stupid to fetch all, then goof with the data,
          # would be better to select only relevant fields, then goof with it
          property_to_int = {
               "Name": 0,
               "Serial Number": 1,
               "Manufacturer": 2,
               "Price": 3,
               "Asset Category": 4,
               "Asset Type": 5,
               "Assigned To": 6,
               "Asset Location": 7,
               "Purchase Date": 8,
               "Install Date": 9,
               "Replacement Date": 10,
               "Notes": 11
               
          }
          months = {
                    "01": "January",
                    "02": "February",
                    "03": "March",
                    "04": "April",
                    "05": "May",
                    "06": "June",
                    "07": "July",
                    "08": "August",
                    "09": "September",
                    "10": "October",
                    "11": "November",
                    "12": "December"
               }
          vals = {}
          raw_data = fetch_all()
          if name == "Notes":  # for notes, we separate into has notes, or doesn't have notes
               vals["Some Notes"] = 0
               vals["No Notes"] = 0
               for obj in raw_data:  
                    if obj.notes == "":
                         vals["No Notes"] += 1
                    else:
                         vals["Some Notes"] += 1
          # should sort this list, so it makes sense when viewing...
          elif name == "Purchase Date":  # all data should be like: 2024-09-24
               raw_data = sorted(raw_data, key=lambda x: x.purchasedate)
               for obj in raw_data:
                    # use to have: - {months[obj.purchasedate[5:7]]}
                    value = f"{obj.purchasedate[:4]}"
                    if value not in vals:
                         vals[value] = 1
                    else:
                         vals[value] += 1
          elif name == "Install Date":  
               sorted(raw_data, key=lambda x: x.installdate)
               for obj in raw_data:
                    value = f"{obj.installdate[:4]}"
                    if value not in vals:
                         vals[value] = 1
                    else:
                         vals[value] += 1
          elif name == "Replacement Date":  
               raw_data = sorted(raw_data, key=lambda x: x.replacementdate)
               for obj in raw_data:
                    value = f"{obj.replacementdate[:4]}"
                    if value not in vals:
                         vals[value] = 1
                    else:
                         vals[value] += 1
               
          else:
               for obj in raw_data:
                    for count, data in enumerate(obj):
                         if count == property_to_int[name]:
                              if data not in vals:
                                   vals[data] = 1
                              else:
                                   vals[data] += 1
          return vals
          
# https://stackoverflow.com/questions/60659643/how-to-change-the-background-colour-of-a-cell-in-a-qcalendarwidget-using-an-sql 
# https://www.pythonguis.com/tutorials/plotting-matplotlib/
