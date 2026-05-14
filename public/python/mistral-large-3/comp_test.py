def main():
    ws_comp_val = 12
    ws_comp_val *= 2
    print(f"COMP: {ws_comp_val}")

    ws_disp_val = ws_comp_val
    print(f"DISP: {ws_disp_val}")

    ws_dyn_disp_val = f"{ws_comp_val:>3}"
    print(f"DYNA: {ws_dyn_disp_val}")

    ws_input = input("INPUT: ")
    print(f"INPUT: {ws_input}")

    ws_comp_val = int(ws_input)
    print(f"COMP: {ws_comp_val}")

if __name__ == "__main__":
    main()
