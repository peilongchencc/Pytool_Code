# gradio


## 定义文本框大小:

```python
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=1, placeholder="Name Here..."), # 定义文本框大小
    outputs="text",
)
demo.launch()
```

由 `lines` 的数值大小定义文本框大小。<br>

## 滑块和点击:

```python
import gradio as gr

def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=["text", "number"],
)
demo.launch()
```

![image](./滑块和点击_code.jpg)


![image](./滑块和点击_web.jpg)