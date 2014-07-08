// Playground - noun: a place where people can play

import Cocoa

extension NSString {
    func isRotationOf(s1: NSString) -> Bool {
        return false
    }
}

/*
 * Test cases
 */

//Two identical strings; a rotation of 0, repeating pattern
"ABCDEFGABCDEFG".isRotationOf("ABCDEFGABCDEFG")

//A rotation of 1, repeating pattern
"BCDEFGABCDEFGA".isRotationOf("ABCDEFGABCDEFG")

//A rotation of 1, nonrepeating pattern
"BCDEFGA".isRotationOf("ABCDEFG")

//A rotation of 2, repeating pattern
"CDEFGABCDEFGAB".isRotationOf("ABCDEFGABCDEFG")

//A rotation of 2, nonrepeating pattern
"CDEFGAB".isRotationOf("ABCDEFG")

//Nonrotated string, equal length
"0123456789".isRotationOf("ABCDEFGHIJ")

//Nonrotated string, different length
"0123456789".isRotationOf("ABCDEFGH")