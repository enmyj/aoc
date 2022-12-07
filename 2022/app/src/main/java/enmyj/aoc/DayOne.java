package enmyj.aoc;

import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Files;

import java.util.*;
import java.util.stream.Collectors;

public class DayOne {
    String filePath = "input_data/dayone.txt";
    List<String> allLines;
    List<Integer> caloriesPerElf = new ArrayList<>();


    public void readInput() {
        try {
            ClassLoader classLoader = getClass().getClassLoader();
            URL resource = classLoader.getResource(filePath);
            if (resource == null) {
                throw new IllegalArgumentException("file not found! " + filePath);
            } else {
                File inputFile = new File(resource.toURI());
                allLines = Files.readAllLines(inputFile.toPath());

            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }

    }

    public void parseInput() {
        Integer caloriesCurrentElf = 0;
        for (String line: allLines) {
            if (line.length() > 0) {
                caloriesCurrentElf += Integer.parseInt(line);
            } else {
                caloriesPerElf.add(caloriesCurrentElf);
                caloriesCurrentElf = 0;
            }
        }
    }

    public Integer calculatePartOne() {
        return Collections.max(caloriesPerElf);
    }

    public Integer calculatePartTwo() {
        List<Integer> sorted = caloriesPerElf.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());
        List<Integer> topThree = sorted.subList(0, 3);
        return topThree.stream().collect(Collectors.summingInt(Integer::intValue));
    }


    public static void main(String[] args) {
        DayOne d = new DayOne();
        d.readInput();
        d.parseInput();
        System.out.println(d.calculatePartOne());
        System.out.println(d.calculatePartTwo());
    }
}
