# Tower Of Hanoi
Python Program To Implement Tower Of Hanoi

![tower_of_hanoi](https://github.com/CsVaidik/TowerOfHanoi/assets/119286887/1329a8cd-9818-445c-9b17-2b84c851b315)

## Introduction
Tower of Hanoi, is a mathematical puzzle which consists of three towers (pegs) and more than one rings is as depicted 
These rings are of different sizes and stacked upon in an ascending order, i.e. the smaller one sits over the larger one. There are other variations of the puzzle where the number of disks increase, but the tower count remains the same.

**Rules**<br/>
The mission is to move all the disks to some another tower without violating the sequence of arrangement. A few rules to be followed for Tower of Hanoi are − <br/>

  -Only one disk can be moved among the towers at any given time.<br/>
  -Only the "top" disk can be removed.<br/>
  -No large disk can sit over a small disk.<br/>

**Base And Recursive Case**<br/>
*Base case:* <br/>

  if n-1<br/>
  
  Move the ring from A to C using B as spare<br/>

*Recursive case:* <br/>

 Move n-1 rings from A to B using C as spare Move the one ring left on A to C using Bus spare<br/>

 Maven-1 rings from B to C using A as spare<br/>


