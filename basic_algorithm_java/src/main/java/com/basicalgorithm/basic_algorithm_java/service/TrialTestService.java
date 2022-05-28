package com.basicalgorithm.basic_algorithm_java.service;

import com.basicalgorithm.basic_algorithm_java.domain.User;
import org.springframework.http.ResponseEntity;

public interface TrialTestService {

    ResponseEntity<Object> runStatusChecking();

    ResponseEntity<Object> runAbout();

    ResponseEntity<Object> introducingPerson(User user);

    ResponseEntity<Object> giveGreetingToUser(String name);
}
