import pytest


def _cell_source(tb, idx):
    return "".join(tb.nb.cells[idx]["source"])


def test_exercise_1_git_workflow(tb):
    source = _cell_source(tb, 3).lower()

    assert "git status" in source
    assert "git add" in source
    assert "git commit" in source
    assert "git push" in source


def test_exercise_2_pep8_refactor(tb):
    out = tb.cell_output_text(5)
    assert "88.5" in out

    source = _cell_source(tb, 5)
    assert "CalcAverage" not in source
    assert "Total=" not in source
    assert "Numbers" not in source


def test_exercise_3_pandas_dataframe(tb):
    # exercise 4 also defines `df` later in the notebook, so re-run this
    # exercise's cell to make sure `df` refers to the orders DataFrame
    tb.execute_cell(7)

    tb.inject("_total_list = df['total'].tolist()")
    assert tb.ref("_total_list") == pytest.approx([13.5, 40.0, 12.0, 4.5])

    tb.inject("_big_orders_customers = big_orders['customer'].tolist()")
    assert tb.ref("_big_orders_customers") == ["Bob"]

    tb.inject("_spend_per_customer = spend_per_customer.to_dict()")
    spend_per_customer = tb.ref("_spend_per_customer")
    assert spend_per_customer["Alice"] == pytest.approx(25.5)
    assert spend_per_customer["Bob"] == pytest.approx(40.0)
    assert spend_per_customer["Carol"] == pytest.approx(4.5)


def test_exercise_4_capstone(tb):
    # exercise 3 also defines `df`, so re-run this exercise's cell to make
    # sure `df` refers to the expenses DataFrame
    tb.execute_cell(9)

    # one row ("2026-03-02,Food,oops") has an invalid amount and is skipped
    tb.inject("_df_len = len(df)")
    assert tb.ref("_df_len") == 6

    tb.inject("_over_budget_sum = int(df['over_budget'].sum())")
    assert tb.ref("_over_budget_sum") == 2

    tb.inject("_totals = df.groupby('category')['amount'].sum().to_dict()")
    totals = tb.ref("_totals")
    assert totals["Food"] == pytest.approx(83.0)
    assert totals["Transport"] == pytest.approx(27.5)
    assert totals["Entertainment"] == pytest.approx(85.0)
