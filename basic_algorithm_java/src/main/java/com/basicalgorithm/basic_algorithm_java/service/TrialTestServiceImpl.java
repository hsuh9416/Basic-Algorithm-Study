package com.basicalgorithm.basic_algorithm_java.service;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class TrialTestServiceImpl implements TrialTestService{


    /**
     * Return message if status is normal
     *
     * @return String message to confirm process running normally
     */
    @Override
    public ResponseEntity<Object> runStatusChecking() {

        String message = "Hello! If you have received this message, the code is now running normally:)";

        return ResponseEntity.status(HttpStatus.OK).body(message);
    }
}
