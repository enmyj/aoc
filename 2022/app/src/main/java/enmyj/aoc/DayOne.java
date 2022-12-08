package enmyj.aoc;

import java.io.*;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;

import java.util.*;
import java.util.stream.Collectors;

public class DayOne {
    String filePath = "input_data/dayone.txt";
    List<String> allLines = new ArrayList<>();
    List<Long> caloriesPerElf = new ArrayList<>();


    public void readInput() {
        ClassLoader classLoader = getClass().getClassLoader();
        InputStream inputStream = classLoader.getResourceAsStream(filePath);

        if (inputStream == null) {
            throw new IllegalArgumentException("file not found! " + filePath);
        }

        try (InputStreamReader streamReader =
                     new InputStreamReader(inputStream, StandardCharsets.UTF_8);
             BufferedReader reader = new BufferedReader(streamReader)) {

            String line;
            while ((line = reader.readLine()) != null) {
                allLines.add(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void parseInput() {
        long caloriesCurrentElf = 0;
        for (String line: allLines) {
            if (line.length() > 0) {
                caloriesCurrentElf += Long.parseLong(line);
            } else {
                caloriesPerElf.add(caloriesCurrentElf);
                caloriesCurrentElf = 0;
            }
        }
        if (caloriesCurrentElf > 0) {
            caloriesPerElf.add(caloriesCurrentElf);
        }
    }

    public Long calculatePartOne() {
        return Collections.max(caloriesPerElf);
    }

    public Long calculatePartTwo() {
        List<Long> sorted = caloriesPerElf.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());
        List<Long> topThree = sorted.subList(0, 3);
        return (long) topThree.stream().mapToInt(Long::intValue).sum();
    }


    public static void main(String[] args) {
        DayOne d = new DayOne();
        d.readInput();
        d.parseInput();
        System.out.println(d.calculatePartOne());
        System.out.println(d.calculatePartTwo());
    }
}
