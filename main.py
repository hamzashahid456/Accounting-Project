import mysql.connector
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from kivymd.uix.dialog import MDDialog

from kivymd.uix.picker import MDDatePicker


class Connection(object):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='accounts_data',
                                             user='faizan',
                                             password='1234'
                                             )

        get_account = """SELECT * FROM accInfo"""
        get_revenue = "SELECT IncomeStatment.Revenue FROM IncomeStatment"
        get_expense = "SELECT IncomeStatment.Expense FROM IncomeStatment"

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)


    except ValueError as e:
        print("Error while connecting to MySQL", e)


class LoginScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class ChartAccounts(Screen):
    pass


class GeneralJournal(Screen):
    pass


class IncomeStatement(Screen):

    def show_statement(obj):
        ex_total = []
        re_total = []
        cursor = Connection.connection.cursor()
        cursor.execute(Connection.get_expense)
        ex_amounts = cursor.fetchall()

        for i in ex_amounts:
            if i[0] != None:
                ex_total.append(i[0])
        cursor.close()

        cursor = Connection.connection.cursor()
        cursor.execute(Connection.get_revenue)
        re_amounts = cursor.fetchall()
        for i in re_amounts:
            if i[0] != None:
                re_total.append(i[0])
        cursor.close()

        total = sum(re_total) - sum(ex_total)

        cursor = Connection.connection.cursor()
        cursor.execute("SELECT * FROM IncomeStatment")
        data = cursor.fetchall()
        data.append(("[size=20sp][b] EBT [/b][/size]", "", "", total))
        income_statement = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       size_hint=(0.79, 0.79),

                                       # Defining no of rows
                                       rows_num=100,
                                       column_data=[
                                           ("Account Name", dp(30)),
                                           ("Revenue", dp(20)),
                                           ("Expense", dp(20)),
                                           ("", dp(20))
                                       ],
                                       row_data=[
                                           (i[0], i[1], i[2], i[3]) for i in data
                                       ]
                                       )

        obj.add_widget(income_statement)


class EnterData(Screen):
    def on_save(obj, instance, value, date_range):
        obj.ids.date.text = str(value)

    def on_cancel(obj, instance, value):
        pass

    def show_date_picker(obj):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=obj.on_save, on_cancel=obj.on_cancel)
        date_dialog.open()

    def enter_data(obj):
        cursor = Connection.connection.cursor()
        obj.insert = "INSERT INTO data (EntryDate, AccountName, Label, Amount, Memo) VALUES (%s, %s, %s, %s, %s)"
        obj.val = (obj.ids['date'].text, obj.ids['acc_name'].text.lower(),
                   obj.ids['acc_label'].text.lower(),
                   obj.ids['amount'].text.lower(),
                   obj.ids['memo'].text.lower())

        cursor.execute(obj.insert, obj.val)
        Connection.connection.commit()

        accounts = []
        accounts2 = []
        cursor.execute(Connection.get_account)
        result = cursor.fetchall()
        for i in result:
            if (i[1] == 'expense'):
                if (i[0] == obj.ids['acc_name'].text.lower()):
                    accounts.append(i[0])
                    accounts.append(float(obj.ids['amount'].text))
                    obj.insert = "INSERT INTO IncomeStatment (AccountName, Expense) VALUES (%s, %s)"
                    obj.val = (accounts[0], accounts[1])
                    cursor.execute(obj.insert, obj.val)
                    Connection.connection.commit()
                    Connection.connection.cursor().close()
            if (i[1] == 'revenue'):
                if (i[0] == obj.ids['acc_name'].text.lower()):
                    accounts2.append(i[0])
                    accounts2.append(float(obj.ids['amount'].text))
                    obj.insert = "INSERT INTO IncomeStatment (AccountName, Revenue) VALUES (%s, %s)"
                    obj.val = (accounts2[0], accounts2[1])
                    cursor.execute(obj.insert, obj.val)
                    Connection.connection.commit()
                    Connection.connection.cursor().close()

    def close_dialog(self, obj):
        pass


class ShowData(Screen):
    def show_data(obj):
        cursor = Connection.connection.cursor()
        cursor.execute("SELECT * FROM data")
        data = cursor.fetchall()

        g_j_datatable = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                    size_hint=(0.79, 0.79),
                                    # Defining no of rows
                                    rows_num=100,
                                    column_data=[
                                        ("Date", dp(20)),
                                        ("Account Title", dp(30)),
                                        ("Debit", dp(20)),
                                        ("Credit", dp(20)),
                                        ("Memo", dp(40)),
                                    ],
                                    row_data=[
                                        ((i[0], i[1], i[3], " ", i[4]) if i[2] == 'debit'
                                         else (i[0], i[1], " ", i[3], i[4])) for i in data
                                    ],

                                    )

        obj.add_widget(g_j_datatable)


class LoadReport(Screen):
    def load_report(obj):
        cursor = Connection.connection.cursor()
        cursor.execute("SELECT * FROM accInfo")
        data = cursor.fetchall()

        c_a_datatable = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                    size_hint=(0.79, 0.79),

                                    # Defining no of rows
                                    rows_num=100,
                                    column_data=[
                                        ("Account Name", dp(30)),
                                        ("Type", dp(20)),
                                        ("Description", dp(40))
                                    ],
                                    row_data=[
                                        (i[0], i[1], i[2]) for i in data
                                    ]
                                    )

        obj.add_widget(c_a_datatable)


class NewAccount(Screen):
    def make_acc(obj):
        cursor = Connection.connection.cursor()
        obj.insert = "INSERT INTO accInfo (AccountName, Type, Description) VALUES (%s, %s, %s)"
        obj.val = (obj.ids['a_ti'].text.lower(),
                   obj.ids['e_ty'].text.lower(),
                   obj.ids['e_d'].text.lower())

        cursor.execute(obj.insert, obj.val)
        Connection.connection.commit()


class AccountsManagerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        screen = Screen()
        self.helpers_file = Builder.load_file('builder.kv')
        screen.add_widget(self.helpers_file)
        return screen

        # Storing Data

    def on_start(self):
        pass
        # finally:
        # if connection.is_connected():
        #     cursor.close()
        #     connection.close()
        #     print("MySQL connection is closed")


AccountsManagerApp().run()

# Must be one of: ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
# md_bg_color: [5/255,223/255,82/255,0.33]
