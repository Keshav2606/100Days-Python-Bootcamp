from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmender"], "l")
table.add_column("Pokemon Type", ["Electric", "Water", "Fire"], "l")
table.add_autoindex("S. No.")
print(table)

