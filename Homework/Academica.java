package Homework;

public class Academica {
    String name; 
    Integer age;

    Academica(String name ,Integer age){
        name = this.name ;
        age  = this.age;
    }
    void studenSubject(String subject){
        System.out.println("Student : " + name + " age : " + age + " ,with subject : " + subject);
    }
}
