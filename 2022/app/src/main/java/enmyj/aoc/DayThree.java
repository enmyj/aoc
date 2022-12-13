package enmyj.aoc;

import java.util.*;

public class DayThree extends AOCAbstract{

    public DayThree(String filePath) {
        this.filePath = filePath;
    }

    public Set<Character> stringToSet(String str) {
        HashSet<Character> hs = new HashSet<>();
        for(int i = 0; i < str.length(); i++) {
            hs.add(str.charAt(i));
        }
        return hs;
    }

    public Set<Character> intersectionSets(List<Set<Character>> listOfSets) {
        return listOfSets.stream().skip(1)
                .collect(()->new HashSet<>(listOfSets.get(0)), Set::retainAll, Set::retainAll);
    }

    public Integer charToPoints(Character c) {
        int val;
        if (Character.isUpperCase(c)) {
            val = (int) c - 65 + 27;
        } else {
            val = (int) c - 96;
        }
        return val;
    }


    @Override
    public void problemOne() {
        Integer points = 0;
        for (String line: allLines) {
            int mid = line.length() / 2;
            Set<Character> sc = intersectionSets(Arrays.asList(stringToSet(line.substring(0, mid)), stringToSet(line.substring(mid))));
            Integer pts = charToPoints(sc.iterator().next());
            points += pts;
        }
    System.out.println(points);
    }

    @Override
    public void problemTwo() {
        Integer points = 0;
        for (int i=0; i<allLines.size(); i+=3){
            List<String> lines = allLines.subList(i, i+3);
            List<Set<Character>> foo = new ArrayList<>();
            for (String line: lines){
                Set<Character> sc = stringToSet(line);
                foo.add(sc);
            }

            Set<Character> sc = intersectionSets(foo);
            Integer pts = charToPoints(sc.iterator().next());
            points += pts;
        }
        System.out.println(points);
    }


    public static void main(String[] args) {
        DayThree d = new DayThree("input_data/daythree.txt");
        d.readFile();
        d.problemOne();
        d.problemTwo();
    }
}
