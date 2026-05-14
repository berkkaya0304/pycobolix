def main():
    # ws-comp-val pic 999 comp
    ws_comp_val = 12
    
    # multiply ws-comp-val by 2 giving ws-comp-val
    ws_comp_val = ws_comp_val * 2
    print(f"COMP: {ws_comp_val}")

    # ws-disp-val pic 999
    ws_disp_val = str(ws_comp_val).zfill(3)
    print(f"DISP:{ws_disp_val}")

    # ws-dyn-disp-val pic zz9 (Right justified, leading zeros suppressed)
    ws_dyn_disp_val = f"{ws_comp_val:3}"
    print(f"DYNA:{ws_dyn_disp_val}")

    # accept ws-input
    try:
        ws_input = input("INPUT: ")
        # Ensure it fits pic 999 (3 digits)
        ws_input = ws_input[-3:].zfill(3) if ws_input else "000"
    except EOFError:
        ws_input = "000"

    print(f"INPUT: {ws_input}")

    # move ws-input to ws-comp-val
    ws_comp_val = int(ws_input)
    print(f"COMP: {ws_comp_val}")

if __name__ == "__main__":
    main()
