import pytest

from roman import roman_to_int, split_into_groups, find_subtractive_pair, number_to_minimal_roman

class TestRoman:
    # def test_populate(self):
    #     populate_numerals(50)
    #     assert False is True
    
    @pytest.mark.parametrize("roman_str, expected_result",
                                [("XVI", 16),
                                ("XIIIIII", 16),

                                ("XIX", 19),
                                ("XIIIIIIIII", 19),
                                ("XVIIII", 19),

                                ("XXXXIIIIIIIII", 49),
                                ("XXXXVIIII", 49),
                                ("XXXXIX", 49),
                                ("XLIIIIIIIII", 49),
                                ("XLVIIII", 49),
                                ("XLIX", 49),

                                ("MCCCCCCVI", 1606),
                                ("MDCVI", 1606),
                                ])
    def test_roman_to_int(self, roman_str, expected_result):
        assert roman_to_int(roman_str) == expected_result

    @pytest.mark.parametrize("roman_str",
                                [
                                ("IIIIIIIIIIIIIIII"),
                                ("VIIIIIIIIIII"),
                                ("VVIIIIII"),
                                ("VVVI"),

                                ("XVIV"),
                                ("IL")
                                ])
    def test_roman_to_int_error(self, roman_str):
        with pytest.raises(ValueError):
            roman_to_int(roman_str)

    @pytest.mark.parametrize("roman_str, expected_result",
                                [("IVL", [["I", "V"], ["L"]]),
                                ("XVIV", [["X"], ["V"], ["I", "V"]]),
                                ])
    def test_split_groups(self, roman_str, expected_result):
        assert split_into_groups(roman_str) == expected_result

    @pytest.mark.parametrize("number, expected_result",
                                [(4, "IV"),
                                (9, "IX"),
                                (40, "XL"),
                                (90, "XC"),
                                (400, "CD"),
                                (900, "CM"),
                                ])
    def test_find_subtractive_pair(self, number, expected_result):
        assert find_subtractive_pair(number) == expected_result

    @pytest.mark.parametrize("number, expected_result",
                                [(4, "IV"),
                                (9, "IX"),
                                (40, "XL"),
                                (90, "XC"),
                                (400, "CD"),
                                (900, "CM"),
                                (3, "III"),
                                (16, "XVI"),
                                (19, "XIX"),
                                (49, "XLIX"),
                                (1606, "MDCVI"),
                                (95, "XCV"),
                                (41, "XLI"),
                                (2841, "MMDCCCXLI"),
                                (4595, "MMMMDXCV")
                                ])
    def test_number_to_minimal_roman(self, number, expected_result):
        assert number_to_minimal_roman(number) == expected_result

    def test_all_numbers(self):
        invalid = []
        for number in range(1, 10000):
            try:
                x = roman_to_int(number_to_minimal_roman(number))
            except ValueError:
                invalid += [number]
                break


        print(invalid)
        assert invalid == []
