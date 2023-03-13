using System;

public class ScrumMaster {
	private String nombre;
	private String rolSecundario;

	public String GetNombre() {
		return this.nombre;
	}
	public void SetNombre(ref String nombre) {
		this.nombre = nombre;
	}
	public String GetRolSecundario() {
		return this.rolSecundario;
	}
	public void SetRolSecundario(ref String rolSecundario) {
		this.rolSecundario = rolSecundario;
	}
	public ScrumMaster(String nombre, String rolSecundario) {
		this.nombre = nombre;
        this.rolSecundario = rolSecundario;
	}
    public override String ToString() {
		return base.ToString() + "Nombre: "+ nombre.ToString() + "\n"+ "Rol Secundario: "
        + rolSecundario.ToString() + "\n";
	}

}