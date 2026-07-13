# 02_NumPy – Numerical Computing with Python

This folder contains my complete NumPy learning journey, from basics to a real-world case study and a full capstone project. The goal is to build a strong numerical computing foundation before moving on to Pandas and further data science topics.

---

## Learning Objectives

- Understand why NumPy is used in data science and machine learning.
- Work efficiently with multidimensional arrays (creation, reshaping, indexing).
- Apply mathematical operations, broadcasting, aggregation, statistics, and random sampling.
- Handle data from files and perform real-world analysis using NumPy only.
- Complete a beginner-friendly capstone project simulating a real company assignment.

---

## Notebook Roadmap

| No. | Notebook | Focus Area |
|-----|----------|------------|
| 01 | `01_Introduction.ipynb` | What NumPy is, why it’s faster than Python lists, installation/import, basic `np.array()` usage. |
| 02 | `02_Array_Creation.ipynb` | Creating 1D/2D/3D arrays with `zeros`, `ones`, `empty`, `arange`, `linspace`, `eye`, `identity`, `full`. |
| 03 | `03_Array_Attributes.ipynb` | Inspecting arrays with `ndim`, `shape`, `size`, `dtype`, `itemsize`, `nbytes`, and type conversion via `astype`. |
| 04 | `04_Array_Indexing_and_Slicing.ipynb` | 1D/2D/3D indexing, negative indexing, slicing, step slicing, reverse slicing, fancy indexing, and boolean indexing. |
| 05 | `05_Reshaping.ipynb` | Reshaping arrays with `reshape`, `flatten`, `ravel`, `transpose`, `resize`, `squeeze`, `expand_dims`. |
| 06 | `06_Mathematical_Operations.ipynb` | Arithmetic operations and universal functions (`sqrt`, `power`, `abs`, `exp`, `log`, trigonometry). |
| 07 | `07_Broadcasting.ipynb` | Broadcasting rules, shape compatibility, practical examples, and common broadcasting errors. |
| 08 | `08_Aggregate_Function.ipynb` | Aggregations: `sum`, `mean`, `median`, `std`, `var`, `min`, `max`, `argmin`, `argmax`, axis-wise ops, cumulative functions. |
| 09 | `09_Random_Module.ipynb` | Random data generation with `rand`, `randint`, `randn`, `choice`, `shuffle`, `permutation`, and setting `seed`. |
| 10 | `10_Boolean_Masking.ipynb` | Advanced filtering using comparisons, boolean arrays, `where`, `any`, `all`, and dataset filtering. |
| 11 | `11_Sorting_Searching_Unique.ipynb` | Sorting and searching with `sort`, `argsort`, `searchsorted`, `unique`, and `isin`. |
| 12 | `12_Stacking_Splitting_Copy_View.ipynb` | Combining and splitting arrays with `concatenate`, `stack`, `hstack`, `vstack`, `split`, `hsplit`, `vsplit`, and copy vs view. |
| 13 | `13_Linear_Algebra.ipynb` | Linear algebra operations: `dot`, `matmul`, matrix multiplication, determinant, inverse, transpose, eigenvalues (intro). |
| 14 | `14_Statistics.ipynb` | Statistical analysis using percentiles, quantiles, covariance, correlation, and basic histograms. |
| 15 | `15_File_IO.ipynb` | Reading and writing NumPy data with `save`, `load`, `savetxt`, `loadtxt`, and CSV handling. |
| 16 | `16_RealWorld_DataAnalysis.ipynb` | End‑to‑end case study using NumPy only: loading a dataset, cleaning, filtering, statistics, sorting, stacking, and answering business questions. |
| 17 | `17_Numpy_Project.ipynb` | Capstone project: **Student Performance Analysis System** using NumPy to simulate a real company assignment and revise all major concepts. |

---

## Real-World Case Study (Notebook 16)

**Notebook:** `16_RealWorld_DataAnalysis.ipynb`  
**Goal:** Show how NumPy is used in an actual data science workflow, not just in isolated examples.

Key steps:

- Load a dataset from CSV/text using NumPy File I/O.
- Explore and understand the dataset structure.
- Select rows and columns using indexing and slicing.
- Filter data using boolean masking and comparisons.
- Compute descriptive statistics (mean, median, std, min, max, etc.).
- Sort and search data to answer practical questions.
- Use stacking/concatenation where needed.
- Perform basic data cleaning.
- Answer realistic business questions and explain why each NumPy step is useful.

This notebook is structured as a **mini project**:

1. Explain the problem.
2. Write the code.
3. Show the output.
4. Explain the output.
5. Connect each step to real data science usage.

At the end, it:

- Revises the full workflow.
- Explains how this workflow will later translate to Pandas.
- Provides interview questions and practice tasks.
- Updates the NumPy roadmap and readiness for moving to Pandas.

---

## Final Capstone Project (Notebook 17)

**Notebook:** `17_Numpy_Project.ipynb`  
**Project Title:** *Student Performance Analysis System (NumPy‑only)*

Overview:

- Create a realistic student marks dataset and save it as CSV.
- Load and analyse the data using NumPy only (no Pandas).
- Answer 20–25 practical questions, such as:
  - Calculate averages and percentages.
  - Find highest and lowest scorers.
  - Perform subject‑wise analysis.
  - Rank students and find top performers.
  - Identify failing or at‑risk students.
  - Filter using boolean masking.
  - Sort records by marks or other criteria.
  - Search for specific records.
  - Compute statistics and derived columns.
  - Save processed results and generate a final performance report.

Concepts revised during the project:

- Array creation and reshaping.
- Indexing and slicing.
- Broadcasting and mathematical operations.
- Aggregation and statistics.
- Boolean masking, sorting, searching.
- Stacking and splitting.
- File I/O and end‑to‑end workflow thinking.

The project is designed to be:

- Beginner‑friendly.
- Interview‑focused.
- Revision‑oriented.
- Copy‑pasteable and easy to follow in Jupyter.

At the end, the notebook includes:

- Project summary.
- Important interview questions.
- Common mistakes to avoid.
- A compact NumPy cheat sheet.
- A clear statement that the NumPy roadmap is **100% complete**, and how this project prepares the transition to Pandas.

---

## How This Prepares for Pandas

Finishing all 17 notebooks builds:

- Strong intuition for arrays, indexing, and vectorized operations.
- Comfort with numerical computing and basic statistics.
- Experience with real‑world workflows (reading files, cleaning data, answering questions).
- A capstone project that can be shown in interviews or on GitHub as part of a data science portfolio.

The next step in this repository is the `03_pandas` folder, where the same topics will be revisited using Pandas for higher‑level data analysis.
