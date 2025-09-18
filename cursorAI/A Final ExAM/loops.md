

# **📌 While Loop Guide**  
*All variations with examples*  

## **1️⃣ Basic While Loop**  
### **Syntax**  
```python
while [condition]:
    # Code to execute
```  

### **Example: Count 1 to 5**  
```python
count = 1  # Initialize
while count <= 5:  # Condition 
    print(count)  # Body 
    count += 1  # Update 

    note: as its initialize 1, it started from 1.
```  
**Output:**  
```
1
2
3
4
5
```  

---

## **2️⃣ Infinite While Loop**  
### **Syntax**  
```python
while True:  # 🔴 **Runs forever!**
    if [exit_condition]:
        break  # 🛑 Exit manually
```  

### **Example: User Input Check**  
```python
while True:
    user_input = input("Type 'quit' to exit: ")
    if user_input == 'quit':
        break  # Exit loop
```  

---

## **3️⃣ While-Else Loop**  
### **Syntax**  
```python
while [condition]:
    # Code
else:  # Runs if NO `break` occurs
    # Post-loop code
```  

### **Example: Search with Else**  
```python
numbers = [1, 3, 5]
index = 0
while index < len(numbers):
    if numbers[index] == 2:
        print("Found!")
        break
    index += 1
else:  # Triggered if 2 not found
    print("Not found!")  # Output: "Not found!"
```  

---

## **4️⃣ Reverse While Loop (Countdown)**  
### **Syntax**  
```python
while [variable] > [limit]:  # Counts down
    # Code
```  

### **Example: 5 to 1**  
```python
i = 5
while i > 0:  # ✅ Runs while i > 0
    print(i)
    i -= 1  # Decrement
```  
**Output:**  
```
5
4
3
2
1
```  

---

## **5️⃣ While Loop with `i < 0`**  
### **Key Notes**  
- Loop **only runs if `i` starts negative** (e.g., `i = -3`).  
- If `i >= 0` initially, the loop **skips entirely**.  

### **Example: Negative to Zero**  
```python
i = -3
while i < 0:  # 🟣 **Purple = rare condition**
    print(f"Current: {i}")
    i += 1  # Increment toward 0
```  
**Output:**  
```
Current: -3
Current: -2
Current: -1
```  

---

## **⚠️ Common Pitfalls**  
1. **Infinite Loops** (forget to update variable):  
   ```python
   while x < 5:  # ❌ No `x += 1` → runs forever!
       print("Oops!")
   ```  
2. **Zero-Iteration Loops** (condition false initially):  
   ```python
   while False:  # ❌ Never runs
       print("Silent...")
   ```  

---
More Example:

```python
i = 5
while i > 0:
    i -= 1
    print("pre decrease", i)
# Output: [4, 3, 2, 1, 0] 

i = 5
while i > 0:
    print("post decrease", i)
    i -= 1
# Output: [5, 4, 3, 2, 1]   

count = 0
while count <= 5:
    count = count + 1
    print("pre increment", count)
# Output: [1, 2, 3, 4, 5, 6]

count = 0
while count <= 5:
    print("post increment", count)
    count = count + 1
# Output: [0, 1, 2, 3, 4, 5]