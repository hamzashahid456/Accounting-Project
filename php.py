# import mysql.connector
#
# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='accounts_data',
#                                          user='faizan',
#                                          password='1234')
#
#
#     get_Expense = """SELECT accInfo.AccountName, accInfo.Type
#                                 FROM accInfo, data
#                                 WHERE accInfo.Type = 'Expense';"""
#
#
#     get_Revenue = """SELECT accInfo.AccountName, accInfo.Type
#                                 FROM accInfo, data
#                                 WHERE accInfo.Type = 'Revenue';"""
#
#
#
#     with connection.cursor() as cursor:
#         list_of_Expense = []
#         cursor.execute(get_Expense)
#         # Fetch rows from last executed query
#         result1 = cursor.fetchall()
#         for row in result1:
#             if row not in list_of_Expense:
#                 list_of_Expense.append(row)
#
#         print(" \n\n List of all account names with Expense \n ")
#         for i in list_of_Expense:
#             print(i)
#
#
#
#         with connection.cursor() as cursor:
#                 list_of_Revenue = []
#                 cursor.execute(get_Revenue)
#                 # Fetch rows from last executed query
#                 result1 = cursor.fetchall()
#                 for row in result1:
#                     if row not in list_of_Revenue:
#                         list_of_Revenue.append(row)
#
#                 print(" \n\n List of all account names with Revenue")
#                 for i in list_of_Revenue:
#                     print(i)
#
#                 get_all_amounts = """SELECT data.AccountName, data.Amount
#                                                             FROM data;"""
#
#                 with connection.cursor() as cursor:
#                     amounts_of_expense_and_revenue = []
#                     cursor.execute(get_all_amounts)
#                     # Fetch rows from last executed query
#                     result2 = cursor.fetchall()
#                     for row in result2:
#                         if row not in amounts_of_expense_and_revenue:
#                             amounts_of_expense_and_revenue.append(row)
#
#                     print(" \n List of amounts of all revenues and expenses \n ")
#                     list_of_amounts = []
#                     for i in list_of_Expense:
#                         for j in list_of_Revenue:
#                             for k in amounts_of_expense_and_revenue:
#                                 if i[0] == k[0] or j[0] == k[0]:
#                                     if k[1] not in list_of_amounts:
#                                         list_of_amounts.append(k[1])
#
#                     for i in list_of_amounts:
#                         print(i)
#
#
#
#
#
#                 # print(" \n List of all accounts of accInfo! ")
# #
# #         # accInfo
# #         get_all_values_for_accInfo = """SELECT data.AccountName, data.Amount
# #                                             FROM data;"""
# #
# #
# #         with connection.cursor() as cursor:
# #             list_of_names_of_all_accounts_of_accInfo = []
# #             cursor.execute(get_all_values_for_accInfo)
# #             # Fetch rows from last executed query
# #             result2 = cursor.fetchall()
# #             for row in result2:
# #                 if row not in list_of_names_of_all_accounts_of_accInfo:
# #                     list_of_names_of_all_accounts_of_accInfo.append(row)
# #
# #
# #             for i in list_of_names_of_all_accounts_of_accInfo:
# #                 print(i)
# #
# #
# #
# #
# #         print(" \n Income Statement Accounts: \n ")
# #
# #         # Revenue
# #         Revenue_Amount =[]
# #         for row1 in list_of_names_of_all_accounts_of_accInfo:
# #             for row2 in list_of_Revenue:
# #                 if row1[0] == row2[0]:
# #                     Revenue_Amount.append(row1[1])
# #
# #
# #         # Expense
# #         Expense_Amount =[]
# #         for row1 in list_of_names_of_all_accounts_of_accInfo:
# #             for row2 in list_of_Expense:
# #                 if row1[0] == row2[0]:
# #                     Expense_Amount.append(row1[1])
# #
# #
# #         total_revenue = 0
# #         print("Revenue Vlaues: ")
# #         for i in Revenue_Amount:
# #             total_revenue = total_revenue + i
# #             print(i)
# #
# #         total_expense = 0
# #         print("Expense Vlaues: ")
# #         for i in Expense_Amount:
# #             total_expense = total_expense + i
# #             print(i)
# #
# #
# #         print("Total Revenue is: ", total_revenue)
# #         print("Total Expense is: ", total_expense)
# #
# #         print("Total is: ", total_revenue - total_expense)
# #
# #
# #
# #     print("\n")
# #
# #
# #
# #
# #
# #
# #
# except mysql.connector.Error as error:
#     print("Failed to create table in MySQL: {}".format(error))
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # """select accInfo.AccountName, accInfo.Type, data.AccountName, data.Amount
# # from data, accInfo
# # where accInfo.Type = 'Expense' or accInfo.Type = 'Revenue';"""
#

print("\033[1m" + "Faizan")
