# this is where we have the threading stuff, since we have to have two background threads at all times:
# one to lisen for signals, and one to process

# wait do we need 2? am i dumb?

# also, this listening thread is mildly a hack job, since some people say "Oh, don't subclass QThread, you neanderthal, and some people say its ok"
# maybe i'll come back and revisit this sometime <- said by someone who IS NOT coming back to revisit this.

# yes, connections are thread safe!! (https://www.psycopg.org/docs/connection.html) that was sort of my confusion coming from using rust stuff.
# "omg is this thread safe?", "Is this mutable?", "is this the right type to pass?", "Can it be moved between threads?". python just works. I sort of love it for that

# also im not sure if I should be sending like, json "packets" to clients with the changes, but i think that just sending a message like "okay, update your table" and refetching it
# all is valid.
import time
from PyQt5.QtCore import QThread, pyqtSignal
import psycopg2

class PostgresListen(QThread):
    # okay, so pyqtSignals HAVE to be defined here
    notifier = pyqtSignal(str)

    # i cant find the class that is returned. rip type hinting i guess
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.countdown = 0
        self.running = True

    def run(self):
        # yeah this should probably not be the name of the channel :sob:
        self.cursor.execute('LISTEN "new update just dropped";') # tbh i dont love the semicolons. also refresh_trigger is the name of the trigger we WILL make.
        while self.running:
            self.connection.poll()
            if self.connection.notifies:
                if self.countdown == 0:
                    self.notifier.emit("yadda yadaa")
                    # if we aren't waiting, we can refresh the table
                    self.countdown = 5 # user config soon!
                print(self.connection.notifies.pop())
            # it will indeed busy wait...
            time.sleep(1)
            if self.countdown != 0:
                self.countdown -= 1
        
    def stop(self):
        self.running = False
        self.wait()

    # now im thinking about how I want to implement this.
    # if it is refresh everytime, it would get pretty damn annoying if someone was adding a whole bunch of items, and the table was jumping around
    # maybe we can do like, a refresh can only happen once a minute (by default. configurable in settings)
    # and once a refresh occurs, if another one is queued, we set a flag somewhere


# this is run as "postgres" user (aka, owner of db)
# invisman=# create function refresh_db()
# invisman-# returns trigger
# invisman-# language plpgsql
# invisman-# as $function$
# invisman$# begin
# invisman$# perform pg_notify('new update just dropped'::text);
# invisman$# return null;
# invisman$# end;
# invisman$# $function$;
# CREATE FUNCTION
# invisman=# create trigger refresh_trigger after insert or update or delete on main for each statement execute procedure refresh_db();
# CREATE TRIGGER

# okay, so we have to listen to the channel "new update just dropped" LOL. i thought that was the message. whatever, maybe ill change that one day...
