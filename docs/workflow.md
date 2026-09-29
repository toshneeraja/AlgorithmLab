# AlgorithmLab - Workflow & Use Case Documentation

## 1. Workflow Diagram (Flowchart)

This is the overall control flow of the program, from launch to exit.

```mermaid
flowchart TD
    Start([Start: python3 main.py]) --> ShowMenu[Show main menu]
    ShowMenu --> Choice{User enters choice}
    Choice -->|1| Fund[Fundamental Algorithms submenu]
    Choice -->|2| Num[Number and Factoring submenu]
    Choice -->|3| Arr[Array and List Techniques submenu]
    Choice -->|4| Ana[Algorithm Analysis - pick an algorithm]
    Choice -->|5| Ex[Show Examples file]
    Choice -->|6| Exit([Exit program])
    Choice -->|invalid| Retry[Show error, ask again] --> Choice

    Fund --> ShowMenu
    Num --> ShowMenu
    Arr --> ShowMenu
    Ana --> ShowMenu
    Ex --> ShowMenu
```

Each submenu (Fundamental, Number, Array) follows the same internal
pattern:

```mermaid
flowchart TD
    SubStart([Enter submenu]) --> SubMenu[Show submenu options + Back]
    SubMenu --> SubChoice{User choice}
    SubChoice -->|algorithm option| Input[Collect & validate input]
    Input --> Run[Run the algorithm function]
    Run --> Show[Show result + explanation]
    Show --> SubMenu
    SubChoice -->|Back| Return([Return to main menu])
```

## 2. Use Case Diagram

```mermaid
graph LR
    User((Student / User))
    User --> UC1[Run a fundamental algorithm]
    User --> UC2[Run a number/factoring algorithm]
    User --> UC3[Run an array/list technique]
    User --> UC4[Browse algorithm analysis]
    User --> UC5[View sample inputs and outputs]
    User --> UC6[Exit the application]
```

There is only one actor (the student/user running the CLI); there
are no external systems, no database, and no network calls, so no
further actors are needed.

## 3. Sequence Diagram - Example: Running "Factorial"

```mermaid
sequenceDiagram
    participant U as User
    participant M as main.py
    participant V as input_validation.py
    participant F as fundamental.py
    participant C as complexity.py
    participant D as display.py

    U->>M: selects "Factorial" from Module 1 menu
    M->>V: get_non_negative_integer("Enter n: ")
    V->>U: prompts for n
    U-->>V: enters n (e.g. 5)
    V-->>M: returns validated integer n
    M->>F: factorial(n)
    F-->>M: returns 120
    M->>D: print_result("Factorial", 120)
    D-->>U: shows "Result -> Factorial: 120"
    M->>C: get_complexity_info("factorial")
    C-->>M: returns approach/time/space info
    M->>D: print_explanation(info)
    D-->>U: shows approach + complexity
```

## 4. Sequence Diagram - Example: Invalid Input Handling

```mermaid
sequenceDiagram
    participant U as User
    participant M as main.py
    participant V as input_validation.py

    U->>M: selects "Summation of first n numbers"
    M->>V: get_non_negative_integer("Enter n: ")
    V->>U: prompts for n
    U-->>V: enters "abc" (invalid)
    V->>U: "Invalid input. Please enter a valid integer."
    V->>U: prompts again
    U-->>V: enters "5" (valid)
    V-->>M: returns 5
```

## 5. Component/Class Note

This project intentionally has no class diagram: CSE1021 at this
stage covers functions and modules (Unit 2), not object-oriented
design, so AlgorithmLab is written purely with functions grouped
into modules. The closest equivalent is the **component diagram** in
`architecture.md`, which shows how the modules depend on each other.
