#Requirements

**Initially done by:** Team3, Members: Muwaffaq Imam, Talgat Khairov, Eldar Qurbanov 

**Updated by**: 

Team1, Members: Anjasmoro Adi Nugroho, Mario Loescher, Sofiia Yermolaieva

Team2, Members: Konstantin Britikov, Danil Afanasiev, Talgat Khaipov, Abdoulie Kassim

# Glossary

| Term                                                         | Definition                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Innocalendar personal message screen                         | It is a message feed in Telegram chat. (InnoSchedule for an example) |
| University Education Department schedule system or UED schedule system | It is a google doc with the schedule currently used by the University Education Department |

# Use Cases

| Use case name                 | **Subscribe for an initial core program**                    |
| ----------------------------- | ------------------------------------------------------------ |
| **Actors**                    | Students (primary), Bot(secondary)                           |
| **Pre-conditions**            | The student has a telegram account                           |
| **Flow of event**             | 1. The student searches for InnoCalendar bot on telegram.(**B1**)<br />2. The bot shows the greeting message which contains descriptions and helps instructions.<br />3. The student starts the bot.(**B2**)<br />4. The student selects configure schedule command.(**B3**)<br />5. The bot shows the available programs (Bachelor and Master)<br />6. The student clicks on the button with the name of his/her core program name.(**B4**) |
| **Alternative flow of event** | 1. The student cannot find InnoCalendar bot on telegram.<br />1.1 Student writes to the owners of the bot<br />3. Bot doesn’t start<br />3.1 Student checks internet connection<br />4(6). Student writes instead of clicking button<br />4(6).1 Bot says student what student should do |
| **Post conditions**           | The Student is assigned to the core program.                 |


| Use case name                                | **Subscribe to a course**                                    |
| -------------------------------------------- | ------------------------------------------------------------ |
| **ActorsStudents (primary), Bot(secondary)** | Students (primary), Bot(secondary)                           |
| **Pre-conditions**                           | The student has already subscribed the initial core program on Innocalendar system |
| **Flow of event**                            | 1. Student searches Innocalendar from telegram app(**B1**)<br />2. Student opens Innocalendar personal message screen on telegram app Student clicks “Add new course” button(**B2**) <br />3. The bot shows the list of all available elective courses.<br />4.  The student selects one of the listed courses.(**B3**) |
| **Alternative flow of event**                | 1. The student cannot find InnoCalendar bot on telegram.<br />1.1 Student writes to the owners of the bot<br />3(5). Student writes instead of clicking button |
| **Post conditions**                          | 1. System updates the changes<br />2. The Student is assigned to the selected course |
| **Non-behavioural Requirements**             | Updates are consistent on personal message screen            |

| **Use Case name**   | **Receive notification**                                     |
| ------------------- | ------------------------------------------------------------ |
| **Actors**          | Students (primary), Bot(secondary)                           |
| **Pre-conditions**  | The Student is subscribed in some courses. <br />The schedule of the subscribed courses was updated/changed. |
| **Flow of event**   | 1. The user receives the notification                        |
| **Post conditions** | The student got a notification                               |
| **Assumptions**     | The student got a notification                               |

| **Use Case name**   | **Update schedule**                                          |
| ------------------- | ------------------------------------------------------------ |
| **Actors**          | Bot (Primary), UED schedule system (secondary)               |
| **Pre-conditions**  | Access agreement with Innopolis University Education Department on the current semester program schedule |
| **Flow of event**   | 1. System checks for changes in University Education Department current semester program schedule. <br />2. The bot receives and records changes to the database. |
| **Post conditions** | The system sends notifications about changes to the Students |
| **Assumptions**     | 1. There will be no database outage, data loss, and leakage. <br />2. All course changes kept up to date<br />3. The system will update once in two hours from UED schedule system |