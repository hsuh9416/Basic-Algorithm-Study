package com.basicalgorithm.basic_algorithm_java.domain;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;

@AllArgsConstructor
@Builder
@Getter
public class User {
    private String name;
    private int age;
    private String major;


    @Override
    public String toString() {
        return name + " is "+ age +" years old and majored in "+ major + "!\nAm I got right? :)";
    }
}
