# Day 16: Coffee Machine

## Project Description
A command-line coffee vending machine simulator that allows users to order espresso, latte, or cappuccino drinks. The machine tracks resources (water, milk, coffee), processes coin payments with detailed change calculation, and includes service/reporting features for machine maintenance.

## Concepts Covered
- **Functions**: Modular code organization with single-responsibility functions like `process_inserted_coins()`, `check_sufficient_resource_bool()`, `update_resources()`, and `reset_resources()`
- **Dictionaries**: Nested dictionary structures to store menu items with ingredients and costs, and resource tracking
- **Global Variables**: Managing state across functions using `global` keyword for `resources`, `money`, and `continue_coffee_transactions`
- **While Loops**: Main program loop that continues until user chooses to exit
- **Conditional Logic**: Multiple if/elif/else statements for menu selection, resource checking, and payment validation
- **String Formatting**: F-strings for formatted output including currency display and resource reporting
- **Type Conversion**: Converting between dollars/cents and handling integer input for coin counting
- **Import Statements**: Using the `time` module to simulate coffee-making delay with `time.sleep()`
- **Function Parameters & Return Values**: Functions that accept parameters and return processed data (booleans, dictionaries, floats)
- **Dictionary Iteration**: Looping through coin types and calculating change breakdown
- **Floor Division & Modulo Operations**: Mathematical operators for calculating optimal coin distribution in change

## Key Features
- Three coffee options with different ingredient requirements and prices
- Resource management that prevents orders when supplies are insufficient
- Coin-based payment system (quarters, dimes, nickels, pennies)
- **Enhanced change calculation** with breakdown by coin type (quarters, dimes, nickels, pennies)
- Machine reporting showing current resources and profit
- **Service mode** to reset machine resources to factory defaults
- Visual feedback with emoji indicators (☕ 💰)

## What I Learned
This project reinforced the importance of breaking down complex programs into smaller, reusable functions. I enhanced the original project in two key ways:

1. **Detailed Change Calculation**: I implemented a `change_back()` function that determines the optimal breakdown of change using floor division and modulo operations to return the minimum number of coins. The original course solution only displayed the total change amount, but I wanted to simulate a real vending machine experience by showing exactly how many of each coin denomination the user receives. This enhancement also taught me about proper pluralization handling in output strings (e.g., "1 penny" vs "2 pennies").

2. **Service Mode Feature**: I added a `reset_resources()` function and a "service" menu option to simulate machine maintenance. This allows the operator to refill the machine's water, milk, and coffee supplies back to their original levels, making the simulation more realistic and reusable without restarting the program.

Managing state across the program using global variables worked for this scope, though I now understand this approach has limitations for larger applications.

## How to Run
```bash
python main.py
```

## Requirements
No external packages required - uses Python standard library only

## Sample Output
```
What would you like? (espresso/latte/cappuccino/report/service): latte
(Cost in cents): 250
Insert $2.50 in coins.
How many quarters?: 12
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
You inserted a total of 300 cents.
Making coffee...
Coffee is ready!
☕
Don't forget to grab your change!
💰
2 quarters
Would you like to make another selection? Type 'y' for Yes or 'n' for No:
```

## Notes
**Enhancements Beyond Course Requirements:**
1. **Detailed Coin Change Breakdown**: Unlike the course solution which only displays total change, this implementation breaks down exact change by coin denomination (quarters, dimes, nickels, pennies), providing a more realistic vending machine experience. The algorithm uses a greedy approach (largest coins first) which works for US currency denominations.
2. **Brewing Time Simulation**: Added realistic coffee-making delay using `time.sleep()` to enhance user experience and simulate actual machine operation time.

3. **Service Mode**: Added a maintenance feature that allows operators to reset machine resources without restarting the program, simulating real vending machine servicing.

**Future Enhancement Ideas:**
- **Change Inventory Management**: Track change as a limited resource (coins available for making change). The machine would need to refuse transactions or request exact change when coin inventory is low, and the service mode would include restocking change.
- **Bill Acceptance**: Expand payment options to accept small bills ($1, $5, $10) in addition to coins, requiring bill-to-coin conversion logic for change calculation.
- **Digital Payment Integration**: Add modern payment methods like Apple Pay, contactless credit/debit cards, or NFC chip readers to simulate contemporary vending machine technology.
- **Expanded Menu**: Include more beverage options or customization features (extra shots, flavor syrups, etc.).

The global variable usage works for this small project but would need refactoring for a larger application using classes or function parameters instead.

---
*Part of the 100 Days of Code - The Complete Python Pro Bootcamp*