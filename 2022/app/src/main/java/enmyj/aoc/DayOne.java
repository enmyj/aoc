package enmyj.aoc;

import java.util.*;
import java.util.stream.Collectors;

public class DayOne extends AOCAbstract{
    List<Long> caloriesPerElf = new ArrayList<>();

    public DayOne(String filePath) {
        this.filePath = filePath;
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

    @Override
    public void problemOne() {
        System.out.println(Collections.max(caloriesPerElf));
    }

    @Override
    public void problemTwo() {
        List<Long> sorted = caloriesPerElf.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());
        List<Long> topThree = sorted.subList(0, 3);
        System.out.println( (long) topThree.stream().mapToInt(Long::intValue).sum());
    }


    public static void main(String[] args) {
        DayOne d = new DayOne("input_data/dayone.txt");
        d.readFile();
        d.parseInput();
        d.problemOne();
        d.problemTwo();
    }
}
