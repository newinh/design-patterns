# Head First Design Patterns

Summary

### Chapter 1.

**디자인 원칙**
* 애플리케이션에서 달라지는 부분을 찾아내고, 달라지지 않는 부분으로부터 분리 시킨다. (Capsulation BAAM)

  달라지는 부분을 찾아서 나머지 코드에 영향을 주지 않도록 `캡슐화` 합니다.
* 구현이 아닌 인터페이스 맞춰서 프로그래밍한다.
* <U>상속보다는 구성을 활용한다.</U>

Strategy Pattern
* 알고리즘군을 정의하고 각각을 캡슐화하여 교환해서 사용할 수 있도록 만든다.


### Chapter 2.

**디자인 원칙**

* 서로 상호작용을 하는 객체 사이에서는 가능하면 느슨하게 결합하는 디자인을 사용해야 한다.


### Chapter 3.

**디자인 원칙**

* 클래스는 확장에 대해서는 열려 있어야 하지만 코드 변경에 대해서는 닫혀 있어야 한다: *OCP(Open-Closed Principle)*

### Chapter 4. Factory  pattern

**디자인 원칙**

* 추상화된 것에 의존하도록 만들어라. 구상클래스에 의존하도록 만들지 않도록 한다: *의존성 뒤집기 원칙(Dependency Inversion Principle)*


### Chapter 5. Singleton

