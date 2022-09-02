function logName(name: string) {
  console.log(name);
}
logName("HALO");

//terminal>>tsc test.ts => test.js
//terminal>>tsc --init => tsconfig.json
//terminal>>tsc -w test.ts =>감시모드(watch mode)

/*
function calc(lostPoint:any):number
// lostPoint의 타입을 지정해주지 않았지만
// return 값을 분석해 number일 것이라 추론
function calc(lostPoint){
    return 100 - lostPoint;
} */

interface Student {
  readonly studentId: Number;
  // readonly : 읽기전용속성, 객체가 생성될 때 할당된 값은 바꿀 수 없다
  studentName: String;
  age?: Number;
  // ? : optional property 반환값X
  gender: String;
  subject: String;
  courseCompleted: Boolean;
  addComment?: (comment: string) => string;
}

function getStudentInfo(studentId: number): Student {
  return {
    studentId: 1234,
    studentName: "HALO",
    gender: "woman",
    subject: "computer",
    courseCompleted: true,
  };
}
function saveStudentInfo(student: Student) {}
