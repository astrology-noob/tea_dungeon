команды предоставляются System.Data.IDbCommand
его реализация для ms sql - SqlCommand

```c#
using (SqlConnection conn = new(conn_string))
{
	conn.Open()
	SqlCommand com = new();
	command.CommandText = "SELECT * FROM test;";
	command.Connection = conn;
	
	// или
	SqlCommand com1 = new("SELECT * FROM test;", conn);
}
```

1. **ExecuteNonQuery** - insert, update, delete (если не нужно отображать данные, возвращает кол-во (int) изменённых данных)
2. **ExecuteReader** - select (возвращает строки / [[SqlDataReader]]) 
3. **ExecuteScalar** - возвращает одно скалярное значение (select min/max/sum/count)

```c#
using (SqlConnection conn = new(conn_string))
{
	conn.Open()
	SqlCommand com = new();
	command.CommandText = "INSERT INTO users (col1, col2) VALUES (2, 3);";
	command.Connection = conn;
	
	int num = com.ExecuteNonQuery(); // 1
}
```