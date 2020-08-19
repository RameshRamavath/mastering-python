## Multi tasking in Python

* Ability of a Operating system to perform different tasks at the same time
* Example: OS performing Game and Songs at the same time
* *Types of MultiTasking*
  * Process based:
     * Multiple threads running at the same time. Ex: Songs download, Games, File upload
  * Thread based:
     * Single process consisting of multiple tasks. Ex: A game can have multiple tasks (Music, input from user etc)

How to achieve  Multi threading in Python
-

* Use threading module
  * from threading import *
* Ways to create
  
  * without creating class
  * By extending Thread class  - Standard way
  * without extending Thread class
      