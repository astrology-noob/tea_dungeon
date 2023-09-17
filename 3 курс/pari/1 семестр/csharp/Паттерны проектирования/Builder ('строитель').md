Создание объекта подразумевает большое кол-во свойств или большое кол-во этапов. Используется чтобы избежать "загрязнения конструктора" - чтобы не передавать значения, из которых вычисляются свойства, а сразу передавать свойства, например??

Builder является статическим внутренним классом в классе, который реализует.
Билдер имеет поля (обязательные и необязательные - устан. дефолтные значения). Метод Builder принимает значения для обязательных полей и "сеттеры" необязательных значений, которые возвращают сам билдер (благодаря чему можно делать цепочки сеттеров)

метод build() возвращает сам объект, а не билдер

```c# 
public class NutritionFacts {  
  private int servingSize;  
  private int servings;  
  private int calories;  
  private int fat;  
  private int sodium;  
  private int carbohydrate;  

  // класс билдер (можно объявить и вне класса)
  
  public static class Builder {  
    // Обязательные параметры  
    private int servingSize;  
    private int servings;  
    
    // Дополнительные параметры - инициализируются значениями по умолчанию  
    private int calories = 0;  
    private int fat = 0;  
    private int carbohydrate = 0;  
    private int sodium = 0;  

   // обязательные параметры получаются в конструкторе
    public Builder(int servingSize, int servings) {  
      this.servingSize = servingSize;  
      this.servings = servings;  
    }  

   // сеттеры значений, возвращается билдер для возможности создания цепочек
    public Builder calories(int val) {  
      calories = val;  
      return this;  
    }  
  
    public Builder fat(int val) {  
      fat = val;  
      return this;  
    }  
  
    public Builder carbohydrate(int val) {  
      carbohydrate = val;  
      return this;  
    }  
  
    public Builder sodium(int val) {  
      sodium = val;  
      return this;  
    }  
  
  // метод build возвращает объект NutritionFacts, который принимает в конструктор объект билдера, а затем принимает все значения параметров
    public NutritionFacts build() {  
      return new NutritionFacts(this);  
    }  
  }  
  
  // конструктор NutritionFacts, который принимает на вход Builder
  private NutritionFacts(Builder builder) {  
    servingSize = builder.servingSize;  
    servings = builder.servings;  
    calories = builder.calories;  
    fat = builder.fat;  
    sodium = builder.sodium;  
    carbohydrate = builder.carbohydrate;  
  }  
}


NutritionFacts cocaCola = new NutritionFacts.Builder(240, 8).calories(100).sodium(35).carbohydrate(27).build();
```

Является альтернативой для Telescoping constructor и JavaBeans

##### Telescoping constructor
Создание нескольких конструкторов с возрастающим кол-вом входных параметров (на каждый случай входных данных)
Минусы:
1) Большое кол-во параметров, легко запутаться
2) Плохо читаемый

##### JavaBeans
Создание пустого конструктора и вызов необходимых сеттеров
Плюс: более читаемый, чем Telescoping constructor
Минусы:
1) Нестабильное состояние объекта между вызовами сеттеров
2) Невозможность реализовать immutable (неизменяемые) классы