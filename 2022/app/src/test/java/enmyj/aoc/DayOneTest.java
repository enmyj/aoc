package enmyj.aoc;

import net.jqwik.api.*;
import net.jqwik.api.constraints.NumericChars;
import net.jqwik.api.constraints.StringLength;
import org.junit.jupiter.api.Assertions;

import java.util.Arrays;
import java.util.List;

import static org.hamcrest.Matchers.*;
import static org.hamcrest.MatcherAssert.assertThat;

class DayOneTest {
    @Example
    void parseInputStatic() {
        DayOne classUnderTest = new DayOne();
        classUnderTest.allLines = Arrays.asList("1", "2", "3", "", "1", "2");
        classUnderTest.parseInput();
        assertThat(Arrays.asList(6L, 3L), equalTo(classUnderTest.caloriesPerElf));
    }

    @Property
    void parseInputDynamic(@ForAll List<@NumericChars @StringLength(min=0, max=10) String> inputLines) {
        DayOne classUnderTest = new DayOne();
        classUnderTest.allLines = inputLines;
        classUnderTest.parseInput();
        assertThat(classUnderTest.caloriesPerElf.size(), lessThanOrEqualTo(inputLines.size()));
    }
}
