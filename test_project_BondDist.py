"""
Tests for geom_analysis.py
"""
import pytest
import project_BondDist as ga

def test_calc_dist():
    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed = ga.calc_dist(coord1, coord2)

    assert observed == 2

def test_bond_chk_true():
    b_length_1 = 1.2
    observed = ga.bond_chk(b_length_1)
    assert observed ==1

def test_bond_chk_false():
    b_length_2 = 2
    observed = ga.bond_chk(b_length_2)
    assert observed ==0

def test_bond_chk_error():
    bond_length = 'a'

    with pytest.raises(TypeError):
        observed = ga.bond_chk(bond_length)
