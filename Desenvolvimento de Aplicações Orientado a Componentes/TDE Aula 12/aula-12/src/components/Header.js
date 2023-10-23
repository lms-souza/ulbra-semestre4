/* eslint-disable jsx-a11y/alt-text */
import './Header.css';

function Header({ title }) {
    return (
      <header className="head">
        <img className="img" src="https://scontent.fccm8-1.fna.fbcdn.net/v/t39.30808-1/295211297_445917077543990_5833620739999901411_n.jpg?stp=c3.0.200.200a_dst-jpg_p200x200&_nc_cat=100&ccb=1-7&_nc_sid=5f2048&_nc_ohc=ANtGWgSbC3sAX_Gzg7H&_nc_ht=scontent.fccm8-1.fna&oh=00_AfAGq50XhtQ93Wx_BXchoEpiqika402dd55tnJ4R14kV8w&oe=65361462"/>
          
      <h1 className="headTitle">{title}</h1>
      </header>
  )
}

export default Header;
