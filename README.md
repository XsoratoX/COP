# Context Oriented Programming(COP)

## What is the Context Oriented Programming?

Context Oriented Programming(COP) is the programming method to modularize behavior depend on context. Several COP languages have been proposed with the increase in COP. I will show an example of program which is used COP with Java programming language.


## What is the Context of COP?

Context is the external environment and internal condition that programs can observe. It is changed according to time and a place. It is also referred to the thing which affect executing various entities of programs. Many COP languages have a **_layer_** and **_layer activation_** as language elements. The layer is the component to modularize behavior corresponding to context. The layer activator is the components to change behavior according to context.

## Example using COP

I will show simple program using COP. This program is written in Java. The program express the automatic air conditioner system, which changes heater and cooler functions according to temperature.
The automatic air conditioner system architecture is shown below.
Heater and Cooler classes are layers. Activator is layer activation. This system's context is temperature. Decision class is to decide whether switching heater, cooler, off. Activator actual changes functions of air conditioner.

![Automatic air conditioner system architecture](https://github.com/XsoratoX/COP/blob/COP/main/figure/air_conditioner.png)