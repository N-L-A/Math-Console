#  Math-Console

A **Python REPL designed for calculations**—simple, fast, programmable, and always ready for action.

> Whether you’re a programmer, engineer, or scientist, everyone needs a calculator that doesn’t get in your way. **Math-Console** is a powerful, Python-based programmable calculator that blends the versatility of Python 3 with the reliability of a modern scientific calculator. Perform anything from simple arithmetic to complex simulations, using precise decimals, fractions, and more—all in an intuitive, scriptable environment.  
>  
> **Features:**  
> - Lightning-fast calculations  
> - Built-in Python 3 language support  
> - Save/load calculation history  
> - Share scripts and research easily  

---

##  Why Math-Console?

There are many math tools out there—from basic calculator apps to heavyweight systems like MATLAB. But most are either **too limited** or **too complex** for everyday use.  
**Math-Console** is designed for _just right_: a sweet spot between capability and simplicity. Most day-to-day calculations are quick equations, not giant spreadsheets or graph plots. So why wrestle with a huge IDE or web tool?

- **No distractions:** Just type as you think.
- **Forgiving:** Make mistakes, get mad at the system—it’ll handle it. (Well, unless you unleash _too much_ fury 🧌)
- **Focus on math:** Not plotting, not endless features—just you and your numbers.

---

##  Documentation

<details>
<summary><strong>Syntax</strong></summary>

- `fa/b`&nbsp;&nbsp;&nbsp;Fraction: write as `3/4` or `5/2`
- `d0.0`&nbsp;&nbsp;&nbsp;Decimal: prefix with `d` for decimal, e.g., `d0.75`
</details>

<details>
<summary><strong>Constants</strong></summary>

- `pi`&nbsp;&nbsp;&nbsp;Mathematical constant π  
- `e`&nbsp;&nbsp;&nbsp;Euler’s number
</details>

<details>
<summary><strong>Commands</strong></summary>

- `hlp()` &nbsp;&nbsp;&nbsp;Prints documentation for non-builtin features  
- `clr()` &nbsp;&nbsp;&nbsp;Clears the console  
- `stdc(prec: int)` &nbsp;&nbsp;&nbsp;Set decimal precision (`prec > 0`)  
- `save_history()` &nbsp;&nbsp;&nbsp;Open file explorer to save history  
- `save_history(path: str = None)` &nbsp;&nbsp;&nbsp;Save history to specified path  
- `load_history()` &nbsp;&nbsp;&nbsp;Open file explorer to load history  
- `load_history(path: str = None)` &nbsp;&nbsp;&nbsp;Load history from specified path  
</details>

<details>
<summary><strong>Functions</strong></summary>

- `rand()` &nbsp;&nbsp;&nbsp;Random decimal in [0, 1)  
- `rand(num: int)` &nbsp;&nbsp;&nbsp;Random integer in [0, num]  
- `rand(num: int, step=s)` &nbsp;&nbsp;&nbsp;Random decimal in [0, num] with step size `s`  
- `rand(min: int/float, max: int/float, step=1)` &nbsp;&nbsp;&nbsp;Random decimal in [min, max] with steps  
    - _Tip:_ Use `loop=x` to get a list of `x` random numbers instead of one  
    - _Note:_ If `step=0`, returns a continuous decimal in the specified range  
- `is_ogre(text: str)` &nbsp;&nbsp;&nbsp;Scans a string for ogre traces. Returns the “ogreish fury level” as an integer (≥ 0), or -1 if no ogre detected  
</details>

---

##  Example Usage

```python
>>> f3/5 + d0.3
0.9
>>> rand(100)
57
>>> stdc(10)
>>> pi
3.1415926536
>>> def func(a, b):
...     return a*(b**2)
... 
>>> func(pi, e)
23.21340436
>>>
