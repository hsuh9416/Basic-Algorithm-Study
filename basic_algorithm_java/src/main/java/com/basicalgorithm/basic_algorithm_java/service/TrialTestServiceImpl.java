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

    /**
     * Explanation of the purpose of development
     *
     * @return String message to explain the purpose of developing
     */
    @Override
    public ResponseEntity<Object> runAbout() {
        String message = "This application is a record of my self-studying about Algorithm and Data Structure"
                + " and practicing developing by Spring boot Framework!";

        return ResponseEntity.status(HttpStatus.OK).body(message);
    }
}
