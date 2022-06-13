# Builder Pattern Example
### The Builder Pattern is a creational pattern whose intent is to separate the construction of a complex object from its representation so that you can use the same construction process to create different representations.
### Lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

### Car Class is
<img src=/screen_shots/ss1.JPG width="423" height="452" >

### Interface class ICarBuilder is:
<img src=/screen_shots/ss2.JPG width="554" height="720" >

### CarBuilder Class implemented from ICarBuilder Class
<img src=/screen_shots/ss3.JPG width="621" height="723" >

### MercedesCarBuilder Class is 
<img src=/screen_shots/ss4.JPG width="551" height="473" >

### AudiCarBuilder Class is 
<img src=/screen_shots/ss5.JPG width="608" height="534" >

### BMWCarBuilder Class is 
<img src=/screen_shots/ss6.JPG width="620" height="600" >

### Main Application Class is 
<img src=/screen_shots/ss7.JPG width="740" height="470" >


### Then finally output is:
<img src=/screen_shots/ss8.JPG width="377" height="733" >

### With help of Builder Pattern:
- You can construct objects step-by-step, defer construction steps or run steps recursively
- You can reuse the same construction code when building various representations of products Single Responsibility Principle
- You can isolate complex construction code from the business logic of the product.
