int[] digits = {1, 2, 5, 4, 4, 5, 2, 3, 6, 5};

var count = digits
    .GroupBy(p => p)
    .Select(g => new {name = String.Format("{0}-hello", g.Key), count = g.Count()}).ToDictionary(x => x.name, x => x.count);

foreach (var dig in count){
    Console.WriteLine(dig);
}