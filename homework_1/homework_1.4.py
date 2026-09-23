"""4. В строке "Ivanou Ivan" поменяйте местами слова: "Ivanou Ivan" => "Ivan Ivanou"""

variable_fio = "Ivanou Ivan"

variable_fio = variable_fio.replace(" Ivan", " Ivanou")
variable_fio = variable_fio.replace("Ivanou", "Ivan", 1)

print(variable_fio)