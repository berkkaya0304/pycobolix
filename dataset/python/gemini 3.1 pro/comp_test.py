def main():
    ws_comp_val = 12
    ws_comp_val *= 2
    
    print(f"COMP: {ws_comp_val:03d}")
    
    ws_disp_val = ws_comp_val
    print(f"DISP:{ws_disp_val:03d}")
    
    ws_dyn_disp_val = ws_comp_val
    print(f"DYNA:{ws_dyn_disp_val:3d}")
    
    print("INPUT: ", end="")
    try:
        ws_input = int(input())
    except ValueError:
        ws_input = 0
        
    print(f"INPUT: {ws_input:03d}")
    
    ws_comp_val = ws_input
    print(f"COMP: {ws_comp_val:03d}")

if __name__ == "__main__":
    main()
