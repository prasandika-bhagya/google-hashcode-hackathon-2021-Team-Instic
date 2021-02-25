package com.vitiya.java;

public class Main {
    public static void main(String[] args) {
        System.out.println("Google Hashcode");
    }
}

/**
 *There are B different books with IDs from 0 to B–1. Many libraries can have a copy of
 * the same book, but we only need to scan each book once. Each book is described by
 * one parameter: the score that is awarded when the book is scanned.
 ***/
class Books { }

/**
 *There are L different libraries with IDs from 0 to L–1. Each library is described by the
 * following parameters:
 * **/
class Library {
    private int libraryId;
    private Books[] books;
    private Time timeTakenForScan;
    private int numberOfBooksScanned;

    public Library(int libraryId, Books[] books, Time timeTakenForScan, int numberOfBooksScanned) {
        this.libraryId = libraryId;
        this.books = books;
        this.timeTakenForScan = timeTakenForScan;
        this.numberOfBooksScanned = numberOfBooksScanned;
    }
}

/**
 * There are D days from day 0 to day D–1. The rst library signup can sta on day 0. D–1
 * is the last day during which books can be shipped to the scanning facility
 * **/
class Time {
    private int numberOfDays;
}

class Scanning {

}