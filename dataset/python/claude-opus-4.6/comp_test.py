"""
COMP Conversion Test
Converted from COBOL (comp_test.cbl) to Python

Demonstrates COBOL COMP (binary) to DISPLAY conversion behavior.
"""


def main():
    ws_comp_val = 12
    ws_comp_val *= 2
    print(f"COMP: {ws_comp_val:03d}")

    ws_disp_val = ws_comp_val
    print(f"DISP:{ws_disp_val:03d}")

    ws_dyn_disp_val = ws_comp_val
    print(f"DYNA:{ws_dyn_disp_val:>3d}")

    ws_input = int(input("INPUT: "))
    print(f"INPUT: {ws_input:03d}")

    ws_comp_val = ws_input
    print(f"COMP: {ws_comp_val:03d}")


if __name__ == "__main__":
    main()
