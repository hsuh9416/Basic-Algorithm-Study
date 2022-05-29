package com.basicalgorithm.basic_algorithm_java.service;

import com.basicalgorithm.basic_algorithm_java.domain.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class TrialTestServiceImpl implements TrialTestService{

    @Autowired
    CommonFunction commonFunction;

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

    /**
     * Introducing person by received data (Post testing)
     *
     * @return String message describing person by given information
     */
    @Override
    public ResponseEntity<Object> introducingPerson(User user) {
        User targetUser = User.builder().name(user.getName()).age(user.getAge()).major(user.getMajor()).build();
        return ResponseEntity.status(HttpStatus.OK).body(targetUser.toString());
    }

    @Override
    public ResponseEntity<Object> giveGreetingToUser(String name) {
        String dayOfWeek = commonFunction.getDayOfWeek(commonFunction.getTodayInfo());
        String greeting = "Hi, "+ name + "! Nice to meet you:) Have a nice "+ dayOfWeek +"!";
        return ResponseEntity.status(HttpStatus.OK).body(greeting);
    }
}
