using System;

public class Integrante {
	private String nombre;
	private String rol;

	public String GetNombre() {
		return this.nombre;
	}
	public void SetNombre(ref String nombre) {
		this.nombre = nombre;
	}
	public String GetRol() {
		return this.rol;
	}
	public void SetRol(ref String rol) {
		this.rol = rol;
	}
	public Integrante(String nombre, String rol) {
		this.nombre = nombre;
        this.rol = rol;
	}
    public override String ToString() {
		return base.ToString() + "\n" + "Nombre: "+ nombre.ToString() + "\n"+ "Rol: "+ rol.ToString() 
		+ "\n";
	}

}