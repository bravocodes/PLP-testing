class Person {
  String name;
  int age;
  String gender;

  Person(this.name,this.age,this.gender);
void DisplayInfo(){
  print("My Name is $name and I am $age years old. I am a $gender");
  }
} 

void main(){
  var person1=Person("Keith",21,"Male");
  person1.DisplayInfo();
}
