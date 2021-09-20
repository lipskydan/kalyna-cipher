# Шифр Калина

Стан шифру описується матрицею 8 x <math>c</math> елементів скінченного розширеного двійкового поля 
<math>GF(2^8)</math>, сформованого незвідним поліномом <math>x^8+x^4+x^3+x^2+1</math>. Кількість раундів та 
кількість рядків у матриці стану наведені у таблиці:

<table>
    <tr>
        <td>#</td>
        <td>Розмір блоку (I) </td>
        <td>Розмір ключа (k)</td>
        <td>Кількість раундів (v)</td>
        <td>Рядків у матриці стану (с)|</td>
        </tr>
    <tr>
        <td>1</td>
        <td rowspan="2">128</td>
        <td>128</td>
        <td>10</td>
        <td rowspan="2">2</td>
      </tr>
    <tr>
        <td>2</td>
        <td>256</td>
        <td>14</td>
      </tr>
    <tr>
        <td>3</td>
        <td rowspan="2">256</td>
        <td>256</td>
        <td>14</td>
        <td rowspan="2">4</td>
      </tr>
    <tr>
        <td>4</td>
        <td>512</td>
        <td>18</td>
      </tr>
    <tr>
    <td>5</td>
    <td>512</td>
    <td>512</td>
    <td>18</td>
    <td>8</td>
  </tr>

</table>

## Зашифрування
#### Перетворення зашифрування описується як

![Test Image 1](imgs_for_readme/1.png)

### Перетворення ![Test Image 1](imgs_for_readme/2.png) , метод KeyExpand.add_round_key_expand() 

Це додавання до матриці стану раундового ключа за модулем <math>2^{64}</math>. При додаванні використовується 
метод запису байтів, при якому інформація в пам'яті зберігається у двійкових даних, розділена на 8 біт (один байт).

### Перетворення &pi;'<sub>l</sub>, метод KeyExpand.sub_bytes()

Перетворення &pi;'<sub>l</sub> — це заміна байтів у матриці стану

#### Підстановки &pi;<sub>0</sub>, &pi;<sub>1</sub>, &pi;<sub>2</sub>, &pi;<sub>3</sub>

Представлені у вигляді багатомірного кортежу S_BOXES_ENC (boxes_and_matrix.py) 

### Перетворення &tau;, метод KeyExpand.shift_rows() 

Перетворення &tau;— це перестановка елементів у матриці (циклічний зсув вправо).

### Перетворення &psi; , метод KeyExpand.mix_columns()
Перетворення &psi;— це лінійне перетворення елементів матриці стану над скінченним полем 
<math>x^8+x^4+x^3+x^2+1</math>

### Перетворення &kappa;<sup>(K<sub>&upsilon;</sub>)</sup>, метод KeyExpand.xor_round_key_expand()

Перетворення &kappa;<sup>(K<sub>&upsilon;</sub>)</sup> — це додавання до матриці стану 
раундового ключа за модулем 2, також відоме як побітове виключне «або» (XOR)

##Розшифрування
Перетворення розшифрування описується як

![Test Image 1](imgs_for_readme/3.png)

Перетворення -1&pi;'<sub>l</sub>, -1&tau;, -1&psi;, -1 ![Test Image 1](imgs_for_readme/2.png) є оберненими 
перетвореннями до перетворень &pi;'<sub>l</sub>, &tau;, &psi;, ![Test Image 1](imgs_for_readme/2.png) 
відповідно.

#### Перетворення -1![Test Image 1](imgs_for_readme/2.png) , метод KeyExpand.sub_round_key_expand()
#### Перетворення -1&pi;'<sub>l</sub>, метод KeyExpand.inv_sub_bytes()
#### Перетворення -1&tau;, метод KeyExpand.inv_shift_rows()
#### Перетворення -1&psi; , метод KeyExpand.inv_mix_columns()
#### Перетворення -1&kappa;<sup>(K<sub>&upsilon;</sub>)</sup>, методKeyExpand.xor_round_key_expand()