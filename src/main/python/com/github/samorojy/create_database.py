import psycopg2
from database_essentials import get_database_connection


def create_database():
    conn = get_database_connection()
    print("Opened database successfully")

    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE Inverted_Index
          (token            TEXT       NOT NULL,
          document_id       INTEGER    NOT NULL);"""
    )

    cur.execute(
        """CREATE TABLE Documents
          (document_id      SERIAL     PRIMARY KEY,
           document_path    TEXT       NOT NULL);"""
    )
    print("Table created successfully")

    cur.execute(
        """ALTER TABLE Inverted_Index
            ADD CONSTRAINT FK_document_id
            FOREIGN KEY (document_id)
            REFERENCES Documents (document_id);
    """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
