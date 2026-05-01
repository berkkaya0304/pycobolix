import { AnalysisResult } from './types';

export const MOCK_DATA: AnalysisResult[] = [
  {
    id: '1',
    source_file: 'PROCESS_PAYROLL.cbl',
    cobol_code: `       IDENTIFICATION DIVISION.
       PROGRAM-ID. PAYROLL.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  GROSS-PAY      PIC 9(5)V99.
       01  TAX            PIC 9(4)V99.
       01  NET-PAY        PIC 9(5)V99.
       PROCEDURE DIVISION.
           COMPUTE GROSS-PAY = 5000.00
           IF GROSS-PAY > 3000.00
               COMPUTE TAX = GROSS-PAY * 0.20
           ELSE
               COMPUTE TAX = GROSS-PAY * 0.15
           END-IF
           COMPUTE NET-PAY = GROSS-PAY - TAX
           DISPLAY "Net Pay: " NET-PAY
           STOP RUN.`,
    cobol_execution_status: 'success',
    timestamp: '2023-10-27T10:00:00Z',
    models: [
      {
        model_name: 'GPT-4o',
        python_filename: 'process_payroll.py',
        python_code: `def calculate_payroll():
    gross_pay = 5000.00
    
    if gross_pay > 3000.00:
        tax = gross_pay * 0.20
    else:
        tax = gross_pay * 0.15
        
    net_pay = gross_pay - tax
    print(f"Net Pay: {net_pay:.2f}")

if __name__ == "__main__":
    calculate_payroll()`,
        status: 'success',
        quality_label: 'High',
        metrics: {
          pylint_score: 9.5,
          complexity_score: 5,
          complexity_reduction_pct: 45,
          pass_at_1: true,
          unit_tests_passed: 5,
          unit_tests_total: 5,
          python_to_cobol_semantic_match_passed: 4,
          python_to_cobol_unit_tests_total: 4,
          python_to_cobol_format_match_passed: 4,
        },
        test_results: [
          { input: '100', expected_output: '100', actual_output: '100', semantic_match: true, format_match: true }
        ],
        python_to_cobol_test_results: [
          { input: '500', expected_output: 'Net Pay: 500.00', actual_output: 'Net Pay:  500.00', semantic_match: true, format_match: false },
          { input: '4000', expected_output: 'Net Pay: 3200.00', actual_output: 'Net Pay: 3200.00', semantic_match: true, format_match: true }
        ],
        invalid_test_results: [
          {
            test_id: 'tc_overflow',
            category: 'overflow',
            description: 'Provide an overly large value for Gross Pay PIC 9(5)V99',
            input: '1234567.89',
            cobol_expected_output: 'Net Pay:  34567.89',
            python_actual_output: 'Net Pay: 1234567.89',
            cobol_faithful: false,
            python_crashed: false,
            exec_time_ms: 25
          },
          {
            test_id: 'tc_alpha_to_numeric',
            category: 'alpha_to_numeric',
            description: 'Provide alpha character to numeric field',
            input: 'ABC',
            cobol_expected_output: 'Net Pay: 00000.00',
            python_actual_output: 'ValueError: could not convert string to float: ABC',
            cobol_faithful: false,
            python_crashed: true,
            exec_time_ms: 15
          }
        ],
        invalid_test_summary: {
          total: 2,
          faithful: 0,
          unfaithful: 1,
          crashed: 1
        }
      },
      {
        model_name: 'x',
        python_filename: 'process_payroll_ds.py',
        python_code: `def process_payroll():
    # x implementation
    pass`,
        status: 'success',
        quality_label: 'Medium',
        metrics: {
          pylint_score: 8.0,
          complexity_score: 8,
          complexity_reduction_pct: 20,
          pass_at_1: true,
          unit_tests_passed: 4,
          unit_tests_total: 5,
          python_to_cobol_semantic_match_passed: 3,
          python_to_cobol_unit_tests_total: 5,
          python_to_cobol_format_match_passed: 2,
        }
      }
    ]
  },
  {
    id: '2',
    source_file: 'INVENTORY.CBL',
    cobol_code: `       IDENTIFICATION DIVISION.
       PROGRAM-ID. INVENTORY.`,
    cobol_execution_status: 'success',
    timestamp: '2023-10-27T11:30:00Z',
    models: [
        {
            model_name: 'x',
            python_filename: 'inventory.py',
            python_code: `def check_inventory():\n    pass`,
            status: 'success',
            quality_label: 'Medium',
            metrics: {
                pylint_score: 8.5,
                complexity_score: 8,
                complexity_reduction_pct: 30,
                pass_at_1: false,
                unit_tests_passed: 0,
                unit_tests_total: 5
            }
        }
    ]
  }
];
