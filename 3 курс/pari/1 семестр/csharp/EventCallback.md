Используется если нужно, чтобы дочерний элемент триггернул родительский на какое-то действие

``` html
<!-- Child Component --> 

<button @onclick="@(() => OnClick.InvokeAsync("Hello from ChildComponent"))">
	Click me
</button>

@code { 
	[Parameter] 
	public EventCallback<string> OnClick { get; set; } 
}
```

``` html
<!-- Parent Component --> 

<ChildComponent OnClick="ClickHandler"></ChildComponent>

<p>@message</p> 

@code { 
	string message = "Hello from ParentComponent"; 
	
	void ClickHandler(string newMessage) 
	{ 
		message = newMessage; 
	} 
}
```

Здесь с помощью OnClick.InvokeAsync из дочернего компонента передаются данные в метод ClickHandler родительского компонента.

То есть мы передаём в доч. комп. родительский хэндлер в виде специального параметра, которому при нажатии на кнопку передаём данные из доч. комп.