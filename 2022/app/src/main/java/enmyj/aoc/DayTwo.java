package enmyj.aoc;

import java.util.HashMap;

public class DayTwo extends AOCAbstract{

    public DayTwo(String filePath) {
        this.filePath = filePath;
    }

    HashMap<String, Integer> myMove = new HashMap<>() {{
        put("X", 1);
        put("Y", 2);
        put("Z", 3);
    }};

    HashMap<String, Integer> targetPoints = new HashMap<>() {{
        put("X", 0);
        put("Y", 3);
        put("Z", 6);
    }};

    HashMap<String, Integer> winLoss = new HashMap<>() {{
        put("A X", 3);
        put("A Y", 6);
        put("A Z", 0);
        put("B X", 0);
        put("B Y", 3);
        put("B Z", 6);
        put("C X", 6);
        put("C Y", 0);
        put("C Z", 3);
    }};

    @Override
    public void problemOne() {
        Integer totalPoints = 0;
        for (String line: allLines) {
            String[] moves = line.split("\\s+");
            totalPoints += winLoss.get(line) + myMove.get(moves[1]);
        }
    System.out.println(totalPoints);
    }

    @Override
    public void problemTwo() {
        Integer totalPoints = 0;
        for (String line: allLines) {
            String[] moves = line.split("\\s+");
            String oppMove = moves[0];
            Integer target = targetPoints.get(moves[1]);
            for (String i: winLoss.keySet()) {
                String oppMoveKey = i.substring(0, 1);
                if (oppMove.equals(oppMoveKey) && target.equals(winLoss.get(i))) {
                    totalPoints += target + myMove.get(i.substring(2));
                }
            }
        }
        System.out.println(totalPoints);
    }


    public static void main(String[] args) {
        DayTwo d = new DayTwo("input_data/daytwo.txt");
        d.readFile();
        d.problemOne();
        d.problemTwo();
    }
}
