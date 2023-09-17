HasRows - метод, чтобы узнать, есть ли результат у запроса вообще

reader.GetName(1) - название второго столбца
reader.Read() / reader.ReadAsync() - читает одну строку

SqlDataReader reader = ExecuteReaderAsync()

reader.GetValue(номер столбца?)

reader.GetValue().GetInt32() - получить опред. тип данных вместо объекта
