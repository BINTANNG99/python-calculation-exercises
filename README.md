# Python Calculation Exercises

I wrote three small command-line programs to practice numeric input, arithmetic, conditional branching, dictionary lookup, and formatted output in Python. The programs calculate employee religious-holiday allowance (THR), adult body mass index (BMI), and a fixed-rate currency conversion. They are exercises rather than production calculators: each one encodes assumptions that need to be stated because several inputs can produce legally, medically, or financially misleading outputs if the program is used outside the exercise context.

| Program | Input | Output |
| --- | --- | --- |
| THR calculator | Months of service, base salary | Calculated THR |
| BMI calculator | Weight in kg, height in m | BMI and category |
| Currency converter | Transaction label, currency, amount | Converted amount |

## THR calculation

The THR program uses months of service $m$ and base salary $W$. For service of at least 12 months, the implemented rule is:

```math
T = W
```

For service below 12 months, the program applies:

```math
T = \frac{m}{12} W
```

where $T$ is the calculated THR. This structure resembles Article 3 of Indonesia's Minister of Manpower Regulation No. 6 of 2016: workers with at least 12 months of continuous service receive one month of wages, while workers with at least one but less than 12 months receive a proportional amount [1]. The same regulation defines one month of wages as either clean wages without allowances or basic wages including fixed allowances, depending on the wage structure [1].

The implementation is therefore not a complete legal THR calculator. It accepts service below one month even though the cited regulation sets eligibility from one month of continuous service, and it uses only `gaji_pokok` as the wage input. If fixed allowances are part of the applicable one-month wage, using base salary alone can produce the wrong amount. Negative months, negative salary, and non-numeric input are also not rejected.

## Adult BMI calculation

The BMI program computes weight $w$ in kilograms divided by squared height $h$ in metres:

```math
B = \frac{w}{h^2}
```

where $B$ is BMI. The categories encoded in the program are below 18.5 as underweight, 18.5 to below 25 as normal, 25 to below 30 as overweight, and 30 or above as obesity. These cutoffs match the broad adult thresholds published by the World Health Organization, although WHO separates obesity into additional classes and uses age-specific assessment for children and adolescents [2].

Because age is not an input, I treat this script as an **adult BMI exercise**, not a general BMI classifier. The program also does not reject zero or negative height, negative weight, or implausible measurements. A zero height raises a division-by-zero error, while negative values can produce output that is mathematically computable but physically meaningless. BMI is used here only to reproduce the encoded category rule; this script is not a medical diagnosis tool.

## Fixed-rate currency conversion

The currency program stores ten currency codes with two hard-coded rates labelled `beli` and `jual`. Its first branch multiplies the entered amount $q$ by the stored buy rate $r_b$:

```math
V_{IDR} = q \cdot r_b
```

Its second branch divides the entered amount by the stored sell rate $r_s$:

```math
V_{FX} = \frac{q}{r_s}
```

Here $V_{IDR}$ is the rupiah result and $V_{FX}$ is the foreign-currency result. The arithmetic itself is simple, but the transaction labels are misleading from the customer's perspective. Bank Indonesia explains that the **sell rate** is the price when a bank sells foreign currency to the customer, while the **buy rate** is the price when a bank buys foreign currency from the customer [3]. In this program, the branch called `buy` converts foreign currency into IDR using the buy rate, which corresponds to the customer selling foreign currency; the branch called `sale` converts an IDR amount into foreign currency using the sell rate, which corresponds to the customer buying foreign currency.

The rates also have no recorded date or source in the program. Bank Indonesia publishes buy and sell transaction rates on each working day [3], so a hard-coded table without provenance should be treated only as exercise data. The input prompt also says only "jumlah uang", although the expected unit changes by branch: the first calculation assumes a foreign-currency amount, while the second assumes an IDR amount. Negative amounts are accepted and no rounding rule specific to each currency is defined.

## Scope and limitations

These programs demonstrate basic Python control flow, but passing a few manual inputs is not enough to establish that they are reliable calculators. No automated tests are included, and boundary cases such as 0, 1, 11, and 12 months of service; BMI values exactly at 18.5, 25, and 30; unsupported currency codes; zero height; or negative amounts are not tested in the current project. The absence of input validation is material because each script accepts values outside the domain assumed by its formula.

The THR formula is incomplete for legal use because wage composition and minimum service eligibility are simplified. The BMI categories are only defensible as adult categories because age is absent. The currency script has a naming error in the transaction direction and uses undated fixed rates. I keep these limitations explicit rather than describing the exercises as payroll, health, or foreign-exchange applications.

## Running the programs

The programs require Python 3 and use only the Python standard library. No third-party package installation is required. Each script is interactive and asks for its required values through the terminal.

```text
python thr_calculator.py
python bmi_calculator.py
python currency_converter.py
```

## References

[1] Kementerian Ketenagakerjaan Republik Indonesia, "Peraturan Menteri Ketenagakerjaan Nomor 6 Tahun 2016 tentang Tunjangan Hari Raya Keagamaan Bagi Pekerja/Buruh di Perusahaan," Mar. 8, 2016. [Online]. Available: https://jdih.kemnaker.go.id/peraturan/detail/1207/peraturan-menteri-nomor-6-tahun-2016. [Accessed: Sep. 8, 2026].

[2] World Health Organization Regional Office for Europe, "Nutrition for a healthy life – WHO recommendations," 2025. [Online]. Available: https://www.who.int/europe/news-room/fact-sheets/item/nutrition---maintaining-a-healthy-lifestyle. [Accessed: Sep. 8, 2026].

[3] Bank Indonesia, "Kurs Transaksi BI." [Online]. Available: https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/default.aspx. [Accessed: Sep. 8, 2026].
