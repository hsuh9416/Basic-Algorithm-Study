package com.basicalgorithm.basic_algorithm_java.domain;

import lombok.AllArgsConstructor;
import lombok.Builder;

@AllArgsConstructor
@Builder
public class User {
    private String name;
    private String age;
    private String major;
}
